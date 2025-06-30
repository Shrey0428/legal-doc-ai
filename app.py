import streamlit as st

st.set_page_config(page_title="Legal Doc AI", layout="wide")
st.title("📄 Legal Document AI Assistant")

uploaded_file = st.file_uploader("Upload a scanned legal PDF", type=["pdf"])
if uploaded_file:
    st.success("✅ File uploaded! (Next: OCR + Extraction)")
