import streamlit as st
import joblib
import pandas as pd
import numpy as np
from category_encoders import TargetEncoder
import xgboost 

# Load trained model and encoders
model_path = r"F:\DS\4th project Tourism Analysis\DATA\XGBoost model.pkl"
ohe_path = r"F:\DS\4th project Tourism Analysis\DATA\One-Hot Endcoder Model.pkl"
target_enc_path = r"F:\DS\4th project Tourism Analysis\DATA\Target Encoder Model.pkl"
scaler_path = r"F:\DS\4th project Tourism Analysis\DATA\Scaler.pkl"

# Load saved models
best_xgb = joblib.load(model_path)
ohe = joblib.load(ohe_path)
target_enc = joblib.load(target_enc_path)
scaler = joblib.load(scaler_path)

st.markdown("""
    <style>
    /* Style the Ratings boxes */
    .Rating-box {
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

    /* Style the "Pretic Rating" button */
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

st.sidebar.header("ℹ️ About The Application")
st.sidebar.write("""
🌟 **Predict Tourism Ratings Easily!**  
Use your visit and attraction info to estimate the tourism experience.

🔹 **How it Works?**  
1️⃣ Fill in your **Visit details**  
2️⃣ Fill in your **Attraction details**  
3️⃣ Click **"🔍 Predict Tourism Rating"**

📊 Instantly get an AI-predicted rating from 1 to 5!

💡 Powered by **Machine Learning**
""")

# Load dataset to create mappings
df_path = r"F:\DS\4th project Tourism Analysis\DATA\Final_Tourim_Table.csv"
df = pd.read_csv(df_path)

# Create mapping dictionaries
country_mapping = dict(zip(df["Country"], df["CountryId"]))
region_mapping = dict(zip(df["Region"], df["RegionId"]))

# Streamlit UI
st.title("🏝️ Tourism Rating Prediction App")
st.write("Enter details below to predict the tourism rating.")

# Select Country & Region
selected_country = st.selectbox("🌍 Select Country", options=df["Country"].unique())
filtered_regions = df[df["Country"] == selected_country]["Region"].unique()
selected_region = st.selectbox("📍 Select Region", options=filtered_regions)

# Convert selected values to corresponding IDs
CountryId = country_mapping[selected_country]
RegionId = region_mapping[selected_region]

# Filter attractions based on selected country and region
filtered_attractions = df[(df["Country"] == selected_country) & (df["Region"] == selected_region)]
attraction_options = filtered_attractions[["AttractionId", "Attraction", "AttractionType"]].drop_duplicates()

# Select Attraction details
selected_attraction_id = st.selectbox("🎡 Select Attraction ID", options=attraction_options["AttractionId"].unique())
selected_attraction_name = st.selectbox("🏞️ Select Attraction Name", options=attraction_options["Attraction"].unique())
selected_attraction_type = st.selectbox("🏛️ Select Attraction Type", options=attraction_options["AttractionType"].unique())

# Other input fields
VisitYear = st.number_input("📅 Visit Year", min_value=2000, max_value=2100, step=1)
VisitMonth = st.number_input("📆 Visit Month", min_value=1, max_value=12, step=1)
VisitModeName = st.selectbox("🚗 Visit Mode Name", options=df["VisitModeName"].unique())

# Prediction button
if st.button("🔍 Predict Rating"):
    # Prepare input data
    input_data = pd.DataFrame({
        "VisitYear": [VisitYear],
        "VisitMonth": [VisitMonth],
        "VisitModeName": [VisitModeName],
        "AttractionId": [selected_attraction_id],
        "Attraction": [selected_attraction_name],
        "AttractionType": [selected_attraction_type],
        "CountryId": [CountryId],
        "RegionId": [RegionId]
    })
    
    # Encoding categorical variables
    encoded_features = ohe.transform(input_data[["VisitModeName", "AttractionType"]])
    encoded_df = pd.DataFrame(encoded_features, columns=ohe.get_feature_names_out(["VisitModeName", "AttractionType"]))
    
    # Encode the target variable
    input_data["Attraction"] = target_enc.transform(input_data["Attraction"])
    
    # Drop original categorical columns
    input_data.drop(columns=["VisitModeName", "AttractionType"], inplace=True)
    
    # Merge with encoded features
    input_data = pd.concat([input_data, encoded_df], axis=1)
    
    # Scale the input data
    input_scaled = scaler.transform(input_data)
    
    # Predict using the trained model
    prediction = best_xgb.predict(input_scaled)
    
    # Display prediction
    st.success(f"⭐ Predicted Tourism Rating: {prediction[0]:.2f}")