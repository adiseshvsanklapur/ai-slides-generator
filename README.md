# AI Slides Generator

Adisesh Venkatesh Sanklapur - July 2025

Automatically generate presentation slides from documents using LLMs.

This project includes a Streamlit frontend and FastAPI backend. It supports both OpenAI (via LlamaIndex) and a fallback local Ollama setup.

## Setup

1. Clone the repo:

```bash
git clone https://github.com/your-username/ai-slides-generator.git
cd ai-slides-generator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
```

---

## Usage

1. Start the FastAPI backend:

```bash
uvicorn src.app.main:app --reload
```

2. In a new terminal, run the Streamlit frontend:

```bash
streamlit run app.py
```

---

## How It Works

- Uploaded files are stored in `/uploads`
- `ContentExtractor` parses raw text based on file type
- `Summarizer` generates bullet points:
  - **OpenAI (default):** Uses LlamaIndex's `GPTVectorStoreIndex` with GPT-4o  
    Text is wrapped as a `Document`, indexed, and queried using a summarization prompt
  - **Ollama (optional):** Local model via CLI (commented out in code)
- `SlideGenerator` builds `.pptx` slides with `python-pptx`
- Final output is saved to `/output/generated_presentation.pptx`

---

## Switching to Ollama (optional)

1. Install Ollama: https://ollama.com
2. Pull a model:

```bash
ollama pull llama3
```

3. In `summarizer.py`, comment out the OpenAI-based code and uncomment the Ollama version.
