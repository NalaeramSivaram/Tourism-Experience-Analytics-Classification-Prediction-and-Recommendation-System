import streamlit as st
import pandas as pd
import joblib

# Load trained model and encoders
model_path = r"F:\DS\4th project Tourism Analysis\DATA\classification\XGBoost model(class).pkl"
ohe_path = r"F:\DS\4th project Tourism Analysis\DATA\classification\One-Hot Endcoder Model(class).pkl"
target_enc_path = r"F:\DS\4th project Tourism Analysis\DATA\classification\Target Encoder Model(class).pkl"
Lable_path = r"F:\DS\4th project Tourism Analysis\DATA\classification\label_encoder(class).pkl"

# Load saved models
best_xgb = joblib.load(model_path)
ohe = joblib.load(ohe_path)
target_enc = joblib.load(target_enc_path)
lable_encoder = joblib.load(Lable_path)

#SET PAGE NAME
st.set_page_config(page_title="Prediting the VisitMode", layout="centered")

st.markdown("""
    <style>
    /* Style the Visitmode boxes */
    .Visitmode-box {
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

    /* Style the "Pretic Visit mode" button */
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
🚗 **Predict Your Ideal Visit Mode!**  
Using AI, we suggest the best **travel mode** for your trip.

🔹 **How it Works?**  
1️⃣ Fill in your **Travel details**  
2️⃣ Click **"🔍 Predict Visit Mode"**  

💡 Powered by **Machine Learning Models**
""")


# Load dataset
df = pd.read_csv(r"F:\DS\4th project Tourism Analysis\DATA\Final_Tourim_Table.csv")
selected_features = ["UserId", "VisitYear", "VisitMonth", "VisitModeId", "AttractionId", "ContinentId", "RegionId", "Attraction", "AttractionType", "AttractionTypeId"]

# Extract Continent, Region, and Country information
continent_data = df[['ContinentId', 'Continent']].drop_duplicates().sort_values('ContinentId')
region_data = df[['RegionId', 'Region']].drop_duplicates().sort_values('RegionId')
country_data = df[['RegionId', 'Country']].drop_duplicates().sort_values('RegionId')

st.title("🎯 Visit Mode Prediction System")
st.write("Predict how a user is likely to visit an attraction based on key details.")

# CREATE THE NUMERIC AND CATEGORICAL INPUT BOXES
col1, col2 = st.columns(2)

with col1:
    user_id = st.selectbox("🆔 User ID", options=df["UserId"].unique())
    visit_year = st.selectbox("📅 Visit Year", options=df["VisitYear"].unique())
    visit_month = st.selectbox("📆 Visit Month", options=df["VisitMonth"].unique())
    visit_modeId = st.selectbox("🚶‍♂️ Visit Mode", options=df["VisitModeId"].unique())
    attraction_id = st.selectbox("📍 Attraction ID", options=df["AttractionId"].unique())

with col2:
    continent_id = st.selectbox("🌍 Continent ID", options=df["ContinentId"].unique())
    region_id = st.selectbox("🏙️ Region ID", options=df["RegionId"].unique())
    attraction = st.selectbox("🎡 Attraction Name", options=df["Attraction"].unique())
    attraction_type = st.selectbox("🎭 Attraction Type", options=df["AttractionType"].unique())
    attraction_type_id = st.selectbox("🆔 Attraction Type ID", options=df["AttractionTypeId"].unique())

# CREATE THE PREDICT BUTTON AND PREDICT THE TARGET WITH HELP OF ENCODER
if st.button("🔍 Predict Visit Mode"):
    if not all([user_id, visit_year, visit_month, visit_modeId, attraction_id, 
                continent_id, region_id, attraction, attraction_type, attraction_type_id]):
        st.error("⚠️ Please enter all the inputs before predicting!")
    else:
        input_data = pd.DataFrame([[user_id, visit_year, visit_month, visit_modeId, attraction_id, 
                                     continent_id, region_id, attraction, attraction_type, attraction_type_id]],
                                  columns=selected_features)

        categorical_features = ["Attraction", "AttractionType"]
        encoded_features = ohe.transform(input_data[categorical_features])
        encoded_df = pd.DataFrame(encoded_features, columns=ohe.get_feature_names_out(categorical_features))

        input_data["Attraction"] = target_enc.transform(input_data[["Attraction"]])

        input_data = input_data.drop(columns=categorical_features)
        input_data = pd.concat([input_data.reset_index(drop=True), encoded_df], axis=1)

        prediction = best_xgb.predict(input_data)
        predicted_category = lable_encoder.inverse_transform(prediction)[0]

        st.success(f"✅ Predicted Visit Mode: **{predicted_category}**")


# CREATE PREVIEW TABLE FOR USER FRIENDLY
st.subheader("📊 Preview of Tourism Data")
st.write("Below is a preview of the tourism dataset used for predictions:")
st.dataframe(df.head(100))

# ADD REFERENCE TABLES FOR USERS
st.subheader("📌 **Continent ID & Name Reference**")
st.table(continent_data)

st.subheader("📌 **Region ID & Name Reference**")
st.table(region_data)

st.subheader("📌 **Country Name Reference (Based on Region ID)**")
st.table(country_data)

