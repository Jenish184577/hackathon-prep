import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("📚 AI Study Assistant")
st.write("Enter any topic and get a summary, quiz and flashcards!")

topic = st.text_input("Enter a topic to study:", placeholder="e.g. Photosynthesis, World War 2, Python loops...")

difficulty = st.selectbox("Select difficulty:", ["Beginner", "Intermediate", "Advanced"])

if topic:
    tab1, tab2, tab3 = st.tabs(["📖 Summary", "❓ Quiz", "🃏 Flashcards"])

    with tab1:
        st.subheader("📖 Summary")
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are an expert teacher who explains topics clearly."},
                {"role": "user", "content": f"Explain {topic} at {difficulty} level in a clear, concise summary of about 150 words."}
            ]
        )
        st.write(response.choices[0].message.content)

    with tab2:
        st.subheader("❓ Quiz Questions")
        response2 = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a teacher who creates quiz questions."},
                {"role": "user", "content": f"Create 5 multiple choice quiz questions about {topic} at {difficulty} level. Include answers."}
            ]
        )
        st.write(response2.choices[0].message.content)

    with tab3:
        st.subheader("🃏 Flashcards")
        response3 = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a teacher who creates flashcards."},
                {"role": "user", "content": f"Create 5 flashcards for {topic} at {difficulty} level. Format as Q: question and A: answer."}
            ]
        )
        st.write(response3.choices[0].message.content)