# Import Libraires
import streamlit as st
import pandas as pd
import joblib

# Load trained model
Model = joblib.load("CBN_GDP.pkl")

st.title("CBN GROSS DOMESTIC PRODUCT (GDP) PREDICTION")

st.write("Enter economic indicators to predict GDP.")

# User inputs
Year = st.number_input("Year", value=2025)

Total_Import = st.number_input("Total Import", value=50000.0)

CEX = st.number_input("Capital Expenditure (CEX)", value=500000.0)

REX = st.number_input("Recurrent Expenditure (REX)", value=300000.0)

Total_Trade = st.number_input("Total_Trade", value=45000.0)

# Prediction button
if st.button("Predict CBN GROSS DOMESTIC PRODUCT (GDP)"):

    input_data = pd.DataFrame({
        'Year':[Year],
        'Total_Import':[Total_Import],
        'CEX':[CEX],
        'REX':[REX],
        'Total_Trade':[Total_Trade]  
    })

    prediction = Model.predict(input_data)

    st.success(
        f"Predicted GDP: {prediction[0]:.2f}%"
    )