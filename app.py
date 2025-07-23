import streamlit as st
import pandas as pd
import joblib

model = joblib.load("water_quality_model.pkl")

st.title("Underground Water Quality Prediction")
st.write("This tool predicts water quality based on simulated sensor data.")

pH = st.number_input("Enter pH value", min_value=0.0, max_value=14.0, value=7.0)
turbidity = st.number_input("Enter Turbidity (NTU)", min_value=0.0, max_value=100.0, value=2.5)
conductivity = st.number_input("Enter Conductivity (µS/cm)", min_value=0.0, max_value=2000.0, value=500.0)

if st.button("Predict"):
    input_data = pd.DataFrame({'pH': [pH], 'Turbidity': [turbidity], 'Conductivity': [conductivity]})
    prediction = model.predict(input_data)
    quality = "Good" if prediction[0] == 1 else "Poor"
    st.success(f"Predicted Water Quality: {quality}")
