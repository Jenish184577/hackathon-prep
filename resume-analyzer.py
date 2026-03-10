import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os 
import PyPDF2
load_dotenv()
client=Groq(api_key=os.getenv("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"))
def extract_text_from_pdf(pdf_file):
    pdf_reader=PyPDF2.PdfReader(pdf_file)
    text=""
    for page in pdf_reader.pages:
        text+=page.extract_text()
    return text 

st.title("AI Resume Analyzer")
st.write("Upload your resume and get instant AI feedback!")

uploaded_file=st.file_uploader("Upload your Resume (PDF)",type="pdf")

if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")
    
    
    resume_text = extract_text_from_pdf(uploaded_file)
    if not resume_text.strip():
        st.error("Could not read text from this PDF. please upload a text based Pdf!")
        st.stop()
    
    st.write("**Analyzing your resume...**")
    
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert HR professional and resume coach with 10 years of experience."
            },
            {
                "role": "user",
                "content": f"""Please analyze this resume and provide:
                1. Overall score out of 10
                2. Top 3 strengths
                3. Top 3 areas to improve
                4. One specific suggestion to make it better
                
                Resume:
                {resume_text}"""
            }
        ]
    )
    
    
    st.subheader("📊 AI Feedback:")
    st.write(response.choices[0].message.content)