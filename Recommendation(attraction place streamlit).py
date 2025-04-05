import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.neighbors import NearestNeighbors

# LOADING THE TOURISM DATASET FROM A CSV FILE INTO A DATAFRAME  
Tourism_df = pd.read_csv(r"F:/DS/4th project Tourism Analysis/DATA/Final_Tourim_Table.csv")

# Create a mapping dictionary: AttractionID -> AttractionName
id_to_name = pd.Series(Tourism_df.Attraction.values, index=Tourism_df.AttractionId).to_dict()

#SET PAGE NAME
st.set_page_config(page_title="Tourism Attraction Recommender", layout="centered")

st.markdown("""
    <style>
    /* Style the recommendation boxes */
    .recommendation-box {
        background-color: #f0f8ff;
        border-left: 5px solid #4682B4;
        padding: 10px 15px;
        margin: 10px 0;
        border-radius: 10px;
        font-size: 18px;
        font-weight: 500;
        color: #333;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
    }

    /* Style the "Get Recommendations" button */
    .stButton>button {
        background-color: #4682B4;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1.2em;
        margin-top: 10px;
    }

    /* Style all h3 headings */
    h3 {
        color: #2F4F4F;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar: App Information
st.sidebar.header("ℹ️ About The Application")
st.sidebar.write("""
🌍 **Discover Your Next Destination!**  
Get personalized **tourist spot** recommendations with ease.  

🔹 **How it Works?**  
1️⃣ Choose your **User ID**  
2️⃣ Click **"🔍 Get Recommendations"**  
3️⃣ Explore **Top 5 Picks** just for you!  

💡 Powered by **AI & Machine Learning**  
""")

#LOAD DATA AND TRAINED MODEL
svd = joblib.load(r"F:\DS\4th project Tourism Analysis\DATA\recommendation\svd.plk")
knn_model = joblib.load(r"F:\DS\4th project Tourism Analysis\DATA\recommendation\KNN.plk")
user_attraction_matrix = joblib.load(r"F:\DS\4th project Tourism Analysis\DATA\recommendation\use attraction matrix")
user_attraction_matrix_reduced = joblib.load(r"F:\DS\4th project Tourism Analysis\DATA\recommendation\user attraction matrix reduce.plk")

# CREATE SELECT BOX FOR INPUT
st.markdown("<h3>Select User ID for Recommendations</h3>", unsafe_allow_html=True)
user_ids = user_attraction_matrix.index.tolist()
user_id = st.selectbox("Choose a User ID", user_ids)

def recommend_attractions(user_id, num_recommendations=5):
    if user_id not in user_attraction_matrix.index:
        return "User ID not found! Try with a different ID."

    user_idx = user_attraction_matrix.index.get_loc(user_id)
    distances, indices = knn_model.kneighbors([user_attraction_matrix_reduced[user_idx]], n_neighbors=7)
    
    similar_users = user_attraction_matrix.index[indices.flatten()[1:]]  # Exclude self

    user_ratings = user_attraction_matrix.loc[user_id]
    unseen_attractions = user_ratings[user_ratings == 0].index  # Attractions user has not rated

    attraction_scores = {}
    for sim_user, dist in zip(similar_users, distances.flatten()[1:]):  # Weighted Similarity
        for attraction in unseen_attractions:
            attraction_scores[attraction] = attraction_scores.get(attraction, 0) + (
                user_attraction_matrix.loc[sim_user, attraction] * (1 - dist)
            )

    recommended_attractions = sorted(attraction_scores, key=attraction_scores.get, reverse=True)[:num_recommendations]
    
    return recommended_attractions if recommended_attractions else "No new recommendations found."

#PREDICT THE RECOMMENDATION 
if st.button("🔮 Get Recommendations"):
    recommended = recommend_attractions(user_id)
    st.markdown("<h3> Recommended Attractions:</h3>", unsafe_allow_html=True)

   # st.write("Recommendation Output", recommended)  
    
if isinstance(recommended, list):
    for i, attraction_id in enumerate(recommended, 1):
        attraction_name = id_to_name.get(attraction_id, "Unknown Name")
        st.markdown(f"<div class='recommendation-box'>✨ ID: {attraction_id} | Name: {attraction_name}</div>", unsafe_allow_html=True)
else:
    st.warning(recommended)

#CREATE PREVIEW TABLE FOR USER FRIENDLY
st.subheader("📊 Preview of Tourism Data")
st.write("Below is a preview of the full tourism dataset used for predictions:")
st.dataframe(pd.read_csv(r"F:/DS/4th project Tourism Analysis/DATA/Final_Tourim_Table.csv"))