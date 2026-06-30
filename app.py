import os
import streamlit as st
import PyPDF2
from google import genai
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and let AI analyze it.")

# --- PASTE YOUR API KEY HERE ---
# Replace the text inside the quotes with the actual long key you copied!
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("Gemini API key not found. Check your .env file.")
    st.stop()
uploaded_file = st.file_uploader(
    "Choose your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("Resume uploaded successfully! ✅")
    
    # Extract text from the PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    extracted_text = ""
    for page in pdf_reader.pages:
        extracted_text += page.extract_text()  
    st.info("AI is analyzing your resume... Please wait a moment. 🤖")
    
    try:
        # Initialize the Gemini Client
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        # Craft a clear prompt for the AI
        prompt = f"""
        You are an expert HR manager and ATS (Applicant Tracking System) reviewer. 
        Analyze the following resume text carefully. Provide:
        1. An overall ATS Score out of 100.
        2. Identified Key Skills.
        3. Clear, bulleted suggestions on how the user can improve their resume for Software Engineering or AIML roles.
        
        Resume Content:
        {extracted_text}
        """
        
        # Call the Gemini 2.5 Flash model
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        # Display the AI results on the app screen
        st.write("## 📊 AI Analysis Result")
        st.write(response.text)
        
    except Exception as e:
        st.error(f"An error occurred while connecting to AI: {e}")