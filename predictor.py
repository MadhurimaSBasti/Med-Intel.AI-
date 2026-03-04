import streamlit as st
import json
from google.oauth2 import service_account
from google.cloud import bigquery

service_account_info = json.loads(st.secrets["gcp_service_account"]["json"])

credentials = service_account.Credentials.from_service_account_info(
    service_account_info
)

client = bigquery.Client(credentials=credentials, project="hospital-160e7")


def predict_diabetes(age, bmi, bp, glucose):

    query = f"""
    SELECT
      predicted_diabetes,
      predicted_diabetes_probs
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
      predicted_HeartDisease,
      predicted_HeartDisease_probs
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