# 🤖 AI Resume Analyzer

AI Resume Analyzer is a Streamlit-based web application that uses Google's Gemini AI to analyze resumes and provide intelligent feedback. Users can upload a PDF resume and receive AI-generated insights to help improve their professional profile and job readiness.

## 🚀 Features

- 📄 Upload PDF resumes
- 🤖 AI-powered resume analysis using Google Gemini
- 🔍 Extracts text from resumes automatically
- 💡 Generates professional feedback and suggestions
- ⚡ Simple and user-friendly Streamlit interface
- 🔐 Secure API key management using `.env`

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini AI
- PyPDF2
- Python Dotenv

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/amruthanelli/AI-Resume-Analyzer.git
```

### 2. Navigate to the Project Directory

```bash
cd "AI Resume Analyzer"
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Configure Gemini API Key

Create a `.env` file in the project root directory.

```env
GEMINI_API_KEY=your_api_key_here
```

Get your Gemini API key from Google AI Studio.

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser automatically.

## 📖 How to Use

1. Launch the application.
2. Upload your resume in PDF format.
3. Wait for the application to extract the content.
4. Gemini AI analyzes the resume.
5. Review the generated feedback and recommendations.

## 🎯 Use Cases

- Students preparing for placements
- Fresh graduates building resumes
- Job seekers improving resume quality
- Career guidance and self-assessment

## 🔮 Future Enhancements

- ATS Score Calculation
- Resume Keyword Analysis
- Job Role Matching
- Resume Improvement Suggestions
- Downloadable Analysis Reports
- Multiple Resume Comparison

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

## 👨‍💻 Author

**Amruthanelli**

GitHub: https://github.com/amruthanelli

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
