"""
app.py — Streamlit UI for AI Slides Generator

Handles file upload, triggers backend slide generation,
and provides a download link for the generated presentation.

Requires backend running at http://127.0.0.1:8000
Endpoints used: /upload/, /generate/, /download/
"""

import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title = "AI Slides Generator", layout = "centered")

st.title("AI Based Auto-Generating Presentation Slides")
st.write("Upload documents and generate slides automatically.")

# File upload widget
uploaded_file = st.file_uploader("Upload a document (.txt, .pdf, .docx, .csv)", type = ["txt", "pdf", "docx", "csv"])

if uploaded_file is not None:
    st.success(f"File '{uploaded_file.name}' uploaded successfully.")

    file = {"file": uploaded_file}
    upload_response = requests.post(f"{BASE_URL}/upload/", files = file)  # Send file to backend

    if upload_response.status_code == 200:
        st.success("File successfully uploaded to the server!")
        if st.button("Generate Slides"):
            generate_slides = requests.get(f"{BASE_URL}/generate/")  # Trigger slide generation

            if generate_slides.status_code == 200:
                st.success("Slides generated successfully!")
                download_url = f"{BASE_URL}/download/?filename=output/generated_presentation.pptx"
                st.markdown(f"[Download Presentation]({BASE_URL}/download/?filename=output/generated_presentation.pptx)", unsafe_allow_html = True)  # Download link
            else:
                st.error("Slide generation failed! Check API logs for more information.")
    else:
        st.error("File upload failed! Please try again.")
