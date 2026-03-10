import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

client = bigquery.Client(
    credentials=credentials,
    project="hospital-160e7"
)


def predict_diabetes(age, bmi, bp, glucose):

    query = f"""
    SELECT
        predicted_diabetes
    FROM ML.PREDICT(
        MODEL `hospital-160e7.healthcare.diabetes_model`,
        (
            SELECT
                {age} AS age,
                {bmi} AS bmi,
                {bp} AS blood_pressure,
                {glucose} AS glucose
        )
    )
    """

    result = client.query(query).to_dataframe()
    return result


def predict_heart(age, bp, chol, hr):

    query = f"""
    SELECT
        predicted_HeartDisease
    FROM ML.PREDICT(
        MODEL `hospital-160e7.healthcare.heart_model`,
        (
            SELECT
                {age} AS age,
                {bp} AS RestingBP,
                {chol} AS Cholesterol,
                {hr} AS MaxHR
        )
    )
    """

    result = client.query(query).to_dataframe()
    return result