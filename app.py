import streamlit as st
import pickle
import pandas as pd

with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 House Price Predictor")

MedInc = st.number_input("Median Income", value=5.0)
HouseAge = st.number_input("House Age", value=20.0)
AveRooms = st.number_input("Average Rooms", value=5.0)
AveBedrms = st.number_input("Average Bedrooms", value=1.0)
Population = st.number_input("Population", value=1000)
AveOccup = st.number_input("Average Occupancy", value=3.0)
Latitude = st.number_input("Latitude", value=35.0)
Longitude = st.number_input("Longitude", value=-120.0)

if st.button("Predict"):

    input_df = pd.DataFrame({
        "MedInc":[MedInc],
        "HouseAge":[HouseAge],
        "AveRooms":[AveRooms],
        "AveBedrms":[AveBedrms],
        "Population":[Population],
        "AveOccup":[AveOccup],
        "Latitude":[Latitude],
        "Longitude":[Longitude]
    })

    prediction = model.predict(input_df)[0]

    st.success(
        f"Predicted House Value: ${prediction*100000:,.2f}"
    )