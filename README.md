# 🤖 AI-RE-MAS
### AI-Powered Requirements Engineering Multi-Agent System

> Transform raw project descriptions into structured SRS documents and Agile user stories — automatically, using a LangGraph-powered multi-agent pipeline backed by Google Gemini.

---

## 📌 Overview

**AI-RE-MAS** is a multi-agent system designed to automate **Requirements Engineering (RE)** — the process of gathering, analyzing, and documenting software requirements. It accepts free-text, PDF, or image input and produces:

- ✅ A complete **Software Requirements Specification (SRS)** document
- ✅ Structured **Agile User Stories**
- ✅ Detection of **ambiguities** and validation notes

---

## 🏗️ Architecture

The system uses a **LangGraph `StateGraph`** to orchestrate 5 specialized AI agents in a sequential pipeline:

```
Input ──► Ingestion ──► Extraction ──► Validation ──► SRS Generator ──► User Story Generator ──► Output
```

### 🔁 Pipeline Flow (`graph/pipeline.py`)

| Step | Agent | Responsibility |
|------|-------|----------------|
| 1 | **Ingestion** | Reads raw text, PDF, or image input; normalizes to clean text |
| 2 | **Extraction** | Identifies functional & non-functional requirements from clean text |
| 3 | **Validation** | Detects ambiguities, contradictions, and missing requirements |
| 4 | **SRS Generator** | Produces a formal SRS document in Markdown format |
| 5 | **User Story Generator** | Converts requirements into Agile user stories |

---

## 📂 Project Structure

```
AI-RE-MAS/
├── agents/
│   ├── ingestion.py        # Input parsing (text / PDF / image via OCR)
│   ├── extraction.py       # Functional & non-functional req. extraction
│   ├── validation.py       # Ambiguity & consistency checking
│   ├── srs_generator.py    # SRS document generation
│   ├── user_story.py       # Agile user story generation
│   └── llm.py              # Shared Gemini LLM client setup
├── graph/
│   └── pipeline.py         # LangGraph StateGraph pipeline definition
├── schemas/
│   └── models.py           # Pydantic state schema (REState)
├── ui/
│   └── app.py              # Streamlit web interface
├── main.py                 # CLI entrypoint
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Prarbdha/AI-RE-MAS.git
cd AI-RE-MAS
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** For PDF and image support, also install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and ensure it's in your system PATH.

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

Get your API key from [Google AI Studio](https://aistudio.google.com/).

---

## ▶️ Usage

### Option A — Streamlit Web UI (Recommended)

```bash
streamlit run ui/app.py
```

Open your browser at `http://localhost:8501`. You can:
- Paste raw text requirements
- Upload a **PDF** or **image** file
- Click **Generate Artifacts** to run the pipeline
- Download the generated SRS as a Markdown file

### Option B — CLI / Script

```bash
python main.py
```

Edit `main.py` to change the input text or file path.

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | Google Gemini (via `langchain-google-genai`) |
| Agent Orchestration | LangGraph |
| State Management | Pydantic (`REState`) |
| PDF Parsing | PyMuPDF (`fitz`) |
| OCR | Tesseract + Pillow |
| Web UI | Streamlit |
| Config | python-dotenv |

---

## 📋 State Schema

All agents share a single Pydantic state object (`REState`):

| Field | Type | Description |
|-------|------|-------------|
| `raw_input` | `str` | Original input text or file path |
| `file_type` | `str` | `text`, `pdf`, or `image` |
| `clean_text` | `str` | Normalized text after ingestion |
| `functional_reqs` | `List[str]` | Extracted functional requirements |
| `non_functional_reqs` | `List[str]` | Extracted non-functional requirements |
| `validation_notes` | `List[str]` | Validation results |
| `ambiguities` | `List[str]` | Detected ambiguous statements |
| `srs_document` | `str` | Generated SRS in Markdown |
| `user_stories` | `List[str]` | Generated Agile user stories |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
