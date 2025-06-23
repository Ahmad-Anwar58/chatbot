import streamlit as st
import openai
from openai import OpenAI

# Setup client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Chat with ChatGPT", page_icon="🤖")
st.title("💬 Chat with ChatGPT")
st.caption("Powered by OpenAI GPT")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Display previous messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Typing..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",  # or "gpt-3.5-turbo"
                    messages=st.session_state.messages,
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"⚠️ Error: {e}"
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
