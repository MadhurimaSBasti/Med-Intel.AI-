import streamlit as st
from predictor import predict_diabetes, predict_heart

st.title("🏥 AI Healthcare Assistant")

st.write("Predict risk for Diabetes or Heart Disease")

disease = st.selectbox(
    "Select prediction type",
    ["Diabetes", "Heart Disease"]
)

age = st.number_input("Age", min_value=1, max_value=120, value=45)

if disease == "Diabetes":

    bmi = st.number_input("BMI", value=30.0)
    bp = st.number_input("Blood Pressure", value=120)
    glucose = st.number_input("Glucose", value=140)

    if st.button("Predict Diabetes Risk"):

        result = predict_diabetes(age, bmi, bp, glucose)

        st.write("Prediction Result:")
        st.dataframe(result)


elif disease == "Heart Disease":

    bp = st.number_input("Resting BP", value=120)
    chol = st.number_input("Cholesterol", value=200)
    hr = st.number_input("Max Heart Rate", value=150)

    if st.button("Predict Heart Disease Risk"):

        result = predict_heart(age, bp, chol, hr)

        st.write("Prediction Result:")
        st.dataframe(result)