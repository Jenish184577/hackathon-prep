import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
client = Groq(api_key="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")

st.title("🤖 My First AI Chatbot")
st.write("Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant named MANN PATEL. You are friendly, funny and talk like a cool friend of jenish . Keep answers short and fun!,mann is very intelligent he got 50 out of 50 in all subjects he studies at nirma universtiy"}
    ]

for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)