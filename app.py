import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-1.5-flash-8b')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
### Instructions:
As an expert in recruitment and natural language processing, your task is to analyze a given job description and resume to provide a 
comprehensive application tracking report. The report should include the following:

1. **Comparison Score**: Calculate the compatibility between the job description and the resume in terms of percentage. 

2. **Missing Keywords**: Identify key skills or experiences missing in the resume.

3. **STAR Statements**: Suggest STAR statements for missing keywords.

resume:{text}
description:{jd}
"""

# Streamlit App UI
st.title("Smart ATS")
st.text("Improve Your Resume ATS")

jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload a PDF")

if st.button("Submit"):
    if uploaded_file:
        with st.spinner("Analyzing your resume..."):
            text = input_pdf_text(uploaded_file)
            formatted_prompt = input_prompt.format(text=text, jd=jd)
            response = get_gemini_response(formatted_prompt)
        st.subheader("AI-Generated Resume Analysis:")
        st.write(response)
