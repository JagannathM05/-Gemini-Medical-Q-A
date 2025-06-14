# Author: Jagannath Malode
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

# Optional helper function to check if a question is medical
def is_medical_question(question):
    medical_keywords = [
        "symptom", "treatment", "diagnosis", "medicine", "disease", "doctor",
        "patient", "infection", "surgery", "virus", "bacteria", "fever",
        "pain", "health", "hospital", "clinic", "prescription", "pharmacy"
    ]
    return any(word in question.lower() for word in medical_keywords)

def get_gemini_response(question):
    if not is_medical_question(question):
        return "⚠️ This application is developed to handle only medical related questions."

    response = model.generate_content(question)
    parts = response.candidates[0].content.parts
    text = ' '.join(part.text for part in parts)
    return text

# Streamlit UI
st.set_page_config(page_title="Q&A Demo")
st.header("🩺 Gemini Medical Q&A")

input = st.text_input("Ask your medical question here:", key="input")
submit = st.button("Submit")

if submit:
    response = get_gemini_response(input)
    st.subheader("Response")
    st.write(response)

