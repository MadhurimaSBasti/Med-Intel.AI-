import streamlit as st
from predictor import predict_diabetes, predict_heart
from rag_engine import ask_health_question

st.title("AI Healthcare Prediction System")

disease = st.selectbox(
    "Select prediction type",
    ["Diabetes", "Heart Disease"]
)

# Common input
age = st.selectbox("Select Age", list(range(18, 100)))

# ------------------ Diabetes ------------------

if disease == "Diabetes":

    bmi = st.selectbox("Select BMI", list(range(15, 50)))
    bp = st.selectbox("Select Blood Pressure", list(range(80, 200)))
    glucose = st.selectbox("Select Glucose Level", list(range(70, 200)))

    if st.button("Predict Diabetes Risk"):

        result = predict_diabetes(age, bmi, bp, glucose)
        prediction = result["predicted_diabetes"][0]

        if prediction == 1:
            st.error("⚠️ The model predicts a HIGH RISK of Diabetes.")
        else:
            st.success("✅ The model predicts a LOW RISK of Diabetes.")


# ------------------ Heart Disease ------------------

elif disease == "Heart Disease":

    bp = st.selectbox("Resting Blood Pressure", list(range(80, 200)))
    chol = st.selectbox("Cholesterol", list(range(120, 350)))
    hr = st.selectbox("Max Heart Rate", list(range(60, 200)))

    if st.button("Predict Heart Disease Risk"):

        result = predict_heart(age, bp, chol, hr)
        prediction = result["predicted_HeartDisease"][0]

        if prediction == 1:
            st.error("⚠️ The model predicts a HIGH RISK of Heart Disease.")
        else:
            st.success("✅ The model predicts a LOW RISK of Heart Disease.")


# ------------------ AI Health Assistant ------------------

st.markdown("---")
st.header("AI Health Assistant")

question = st.text_input("Ask a health question")

if question:
    with st.spinner("Thinking..."):
        answer = ask_health_question(question)

    st.write(answer)