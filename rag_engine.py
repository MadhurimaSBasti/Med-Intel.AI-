from google import genai
import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Gemini client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Medical knowledge
documents = [
    "Diabetes is a chronic condition that affects how the body processes blood sugar.",
    "Common symptoms of diabetes include frequent urination, thirst, fatigue, and blurred vision.",
    "Heart disease refers to conditions affecting the heart and blood vessels.",
    "Risk factors for heart disease include high cholesterol, high blood pressure, smoking, and obesity.",
    "Maintaining a healthy diet and regular exercise can reduce risk of diabetes and heart disease."
]

# Create embeddings
embeddings = model.encode(documents)

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


def ask_health_question(question):

    query_vector = model.encode([question])

    _, indices = index.search(np.array(query_vector), k=2)

    context = " ".join([documents[i] for i in indices[0]])

    prompt = f"""
    Use the following medical information to answer the question.

    Context:
    {context}

    Question:
    {question}
    """

def ask_health_question(question):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=question
        )
        return response.candidates[0].content.parts[0].text
    except:
        return "⚠️ AI assistant temporarily unavailable due to API limits."