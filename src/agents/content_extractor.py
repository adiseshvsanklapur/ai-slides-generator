"""
content_extractor.py — Extracts raw text from various document formats

Supports TXT, PDF, DOCX, and CSV files from a given directory.
Prepares text for summarization and slide generation.
"""

import os
import pandas as pd
import fitz  # PyMuPDF for PDF parsing
from docx import Document
from llama_index.core import SimpleDirectoryReader

class ContentExtractor:
    def __init__(self, directory="data/"):
        self.directory = directory

    def extract_text_from_txt(self, file_path):
        # Read plain text file
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
        
    def extract_text_from_pdf(self, file_path):
        # Extract text from each page in a PDF
        text = ""
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text("text") + "\n"
        return text
    
    def extract_text_from_docx(self, file_path):
        # Extract text from Word document
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    
    def extract_text_from_csv(self, file_path):
        # Convert CSV content to string
        df = pd.read_csv(file_path)
        return df.to_string()
    
    def extract_from_file(self, file_path):
        # Determine file type and extract accordingly
        _, ext = os.path.splitext(file_path)
        if ext == ".txt":
            return self.extract_text_from_txt(file_path)
        elif ext == ".pdf":
            return self.extract_text_from_pdf(file_path)
        elif ext == ".docx":
            return self.extract_text_from_docx(file_path)
        elif ext == ".csv":
            return self.extract_text_from_csv(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
        
    def extract_from_directory(self):
        # Loop over files in directory and extract content
        extracted_data = {}
        if not os.path.exists(self.directory):
            raise FileNotFoundError(f"Directory not found: {self.directory}")
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                try:
                    extracted_data[filename] = self.extract_from_file(file_path)
                except Exception as e:
                    print(f"Error processing {filename}: {e}")
        return extracted_data
    

if __name__ == "__main__":
    extractor = ContentExtractor(directory = "data/")
    extracted_content = extractor.extract_from_directory()

    # Print preview of extracted content
    for file, content in extracted_content.items():
        print(f"\n Extracted content from {file}: \n {content[:500]}...\n")
