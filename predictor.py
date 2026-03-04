from google.cloud import bigquery

client = bigquery.Client()

# Diabetes Prediction
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


# Heart Disease Prediction
def predict_heart(age, bp, chol, hr):

    query = f"""
    SELECT
      predicted_HeartDisease,
      predicted_probability
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