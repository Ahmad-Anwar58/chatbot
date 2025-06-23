# app.py
import streamlit as st
import json
import pandas as pd
from data_loader import load_data
from logic import get_recommendation, get_roi_response

# Load FAQ JSON
with open("faq.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)

# Load Excel Data
data = load_data("System_Data_Cleaned.xlsx")

# Chatbot logic
def get_bot_response(query):
    # Check in FAQ first
    for item in faq_data:
        if query.lower() in item["question"].lower():
            return item["answer"]

    # Custom logic based on dataset
    if "roi" in query.lower():
        return get_roi_response(data)
    if "irrigation" in query.lower() or "water" in query.lower():
        return get_recommendation(data, "Irrigation")
    if "yield" in query.lower():
        return get_recommendation(data, "Yield")

    return "Sorry, I couldn't find an answer. Please ask a farming-related question."

# Streamlit UI
st.set_page_config(page_title="CropIQ Chatbot", layout="centered")
st.title("🌾 CropIQ Farmer Chatbot")
st.markdown("Ask me about your crop, irrigation, fertilizer, yield, ROI, and more!")

user_query = st.text_input("Ask your question:", "How do I increase yield?")

if st.button("Get Answer"):
    response = get_bot_response(user_query)
    st.success(response)
