import streamlit as st


def process_uploaded_file(uploaded_file):
    if uploaded_file is None:
        return ""
    content = ""
    if uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        try:
            from pypdf import PdfReader

            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                content += page.extract_text() + "\n"
        except ImportError:
            st.error("Please install pypdf to process PDF files.")
    return content
