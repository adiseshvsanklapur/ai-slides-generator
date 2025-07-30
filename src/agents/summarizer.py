"""
======================
 Summarizer (OpenAI + LLaMa Index)
======================

summarizer.py — Summarizes raw text into bullet points using LLMs

Uses LlamaIndex + OpenAI's GPT-4o to generate slide-ready summaries
from extracted document text.
"""

import os
from dotenv import load_dotenv
from llama_index.core import GPTVectorStoreIndex, SimpleDirectoryReader, Document
from llama_index.llms.openai import OpenAI
from llama_index.core.settings import Settings

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class Summarizer:
    def __init__(self):
        # Set LLM backend for LlamaIndex
        Settings.llm = OpenAI(model = "gpt-4o", api_key = OPENAI_API_KEY)

    def summarize_text(self, text):
        # Wrap input as LlamaIndex Document
        documents = [Document(text = text)]
        index = GPTVectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()

        # Query LLM for presentation-style bullet summary
        response = query_engine.query("Summarize this text into key bullet points suitable for presentation slides")
        return response.response
    
if __name__ == "__main__":
    sample_text = """The creation of AI has completely changed the way in how people create presentations.
      This project will essentially use the automation that AI provides in order to convert text into slides in a super efficient manner.
        The extracted content will then be summarized utilizing numerous different AI techniques."""
    
    summarizer = Summarizer()
    summary = summarizer.summarize_text(sample_text)
    print("\n **Summarized Text:**\n")
    print(summary)

"""
======================
 Summarizer (Ollama)
======================

summarizer.py — Summarizer (Ollama version)

Uses a local LLM (via Ollama) to convert raw text into bullet points
suitable for presentation slides. No OpenAI APIs used.

Alternative for those who can't access OpenAI API.
"""

# import subprocess

# class Summarizer:
#     def __init__(self, model_name="llama3.2"):  # Replace with your local model name
#         self.model_name = model_name

#     def summarize_text(self, text):
#         prompt = (
#             "Summarize this text into a bunch key bullet points suitable for presentation slides. These bullet points will be directly fed into a presentation slide deck and displayed:\n\n"
#             + text
#         )

#         # Run prompt through local Ollama model
#         result = subprocess.run(
#             ["ollama", "run", self.model_name],
#             input=prompt,
#             capture_output=True,
#             text=True,
#         )

#         if result.returncode != 0:
#             raise RuntimeError(f"Ollama error: {result.stderr}")
#         return result.stdout.strip()


# if __name__ == "__main__":
#     sample_text = """The creation of AI has completely changed the way in how people create presentations.
#     This project will essentially use the automation that AI provides in order to convert text into slides in a super efficient manner.
#     The extracted content will then be summarized utilizing numerous different AI techniques."""

#     summarizer = Summarizer()
#     summary = summarizer.summarize_text(sample_text)
#     print("\n**Summarized Text:**\n")
#     print(summary)