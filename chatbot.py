# chatbot.py ← Main chatbot logic
import streamlit as st
from logic import get_bot_response
from data_loader import load_data, get_summary_stats

st.set_page_config(page_title="CropIQ Chatbot", page_icon="🌾")
st.title("🤖 CropIQ Chatbot for Farmers")
st.markdown("""
Ask questions about your crops, irrigation, fertilizer, ROI, and more.
""")

# Load data and stats
system_data = load_data()
stats = get_summary_stats(system_data)

# Session state for chat
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Welcome! How can I assist you with your crops today?"}
    ]

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask me anything about farming...")
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot reply
    bot_reply = get_bot_response(user_input, system_data, stats)
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
