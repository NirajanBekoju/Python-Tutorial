import streamlit as st
import pandas as pd
import joblib
import numpy as np

model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Heart Disease Prediction App")

st.write("Enter patient details to predict the likelihood of heart disease. This app uses a trained Logistic Regression model.")

st.header("Patient Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (years)", min_value=0, max_value=120, value=50)
    gender = st.selectbox("Gender", options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
    cp = st.selectbox("Chest Pain Type (0-3)", options=[0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=200, value=120)
    chol = st.number_input("Cholesterol (mg/dL)", min_value=0, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    restecg = st.selectbox("Resting ECG (0-2)", options=[0, 1, 2])

with col2:
    thalach = st.number_input("Max Heart Rate (bpm)", min_value=0, max_value=220, value=150)
    exang = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    slope = st.selectbox("Slope of ST Segment (0-2)", options=[0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (0-4)", options=[0, 1, 2, 3, 4])
    thal = st.selectbox("Thalassemia (0-3)", options=[0, 1, 2, 3])


if st.button("Predict"):
    input_data = np.array([[age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    input_data_scaled = scaler.transform(input_data)
    
    prediction = model.predict(input_data_scaled)
    probability = model.predict_proba(input_data_scaled)[0][1] * 100
    
    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.error(f"The model predicts a **high likelihood** of heart disease ({probability:.1f}% probability).")
    else:
        st.success(f"The model predicts a **low likelihood** of heart disease ({100 - probability:.1f}% probability of no disease).")


st.sidebar.header("How to Use")
st.sidebar.write("1. Enter patient details in the form.")
st.sidebar.write("2. Click the 'Predict' button to see the result.")
st.sidebar.write("3. The model predicts whether the patient is likely to have heart disease (1 = Yes, 0 = No).")