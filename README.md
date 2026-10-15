# AI Document Assistant

A Python-based AI application that lets users upload PDF documents, extract their text, and ask questions about the document using Google's Gemini API.

## Features

- Upload PDF documents
- Extract text using PyMuPDF
- Ask questions about document content
- Generate AI-powered answers using Gemini
- Preview extracted text
- Handle missing input and PDF extraction errors

## Technology Stack

- Python
- Streamlit
- PyMuPDF
- Google Gemini API
- Python Dotenv

## Project Structure

```text
AI-Document-Assistant/
├── ai_service.py
├── pdf_service.py
├── streamlit_app.py
├── app.py
├── text_utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/AswathiPA/AI-Document-Assistant.git
cd AI-Document-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment on Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_actual_api_key
```

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

Keep your API key private. Never commit the `.env` file to GitHub.

### 6. Run the application

```bash
python -m streamlit run streamlit_app.py
```

Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Future Improvements

- Retrieval-Augmented Generation (RAG)
- Semantic document search
- Source references in AI answers
- Improved conversation history
- Automated tests and deployment

## Author

Aswathi P A

Developed as a hands-on project to practise Python and Generative AI application development.
