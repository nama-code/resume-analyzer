# Smart ATS (Resume Analyzer)

This is a Streamlit application that uses Google's Gemini API to analyze a resume against a job description.

## Features
- Calculates resume/job description compatibility
- Identifies missing keywords
- Generates STAR format improvement suggestions

## How to Deploy on Hugging Face
1. Create a new Streamlit Space.
2. Upload this project (`app.py`, `requirements.txt`, `README.md`).
3. Go to the "Settings" tab of your Space.
4. Add a secret named `GOOGLE_API_KEY` with your Gemini API key.
5. The app will auto-deploy.

## Notes
- Only PDF resumes are supported.
- You must have a valid Gemini API key from Google AI Studio.
