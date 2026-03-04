import streamlit as st
import json
from google.oauth2 import service_account
from google.cloud import bigquery

service_account_info = json.loads(st.secrets["gcp_service_account"]["json"])

credentials = service_account.Credentials.from_service_account_info(
    service_account_info
)

client = bigquery.Client(credentials=credentials, project="hospital-160e7")