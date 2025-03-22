# NGSS EquityCoach MVP

A Retrieval-Augmented Generation (RAG) chatbot that helps science teachers find and implement NGSS-aligned curriculum materials with equity in mind.

## 🚀 Features
- Lesson search by DCI or phenomenon
- SEP identification
- Modeling support
- Assessment mapping
- Streamlit chat interface
- Warm, teacher-centered coaching tone

## 🧰 Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Set your OpenAI key:

```bash
export OPENAI_API_KEY=sk-xxxxxx  # Windows: set OPENAI_API_KEY=sk-xxxxxx
```

## 🧠 Usage

```bash
python ingest_curriculum.py
python embed_documents.py
streamlit run app.py
```

## 🧪 Chatbot Use Cases
- "Find a 3rd grade lesson about erosion"
- "Where do students engage in modeling?"
- "What SEP is in this investigation?"
