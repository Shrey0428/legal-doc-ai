import streamlit as st
from ocr_module import convert_pdf_to_images, run_ocr_on_image

st.set_page_config(page_title="Legal Doc AI", layout="wide")
st.title("📄 Legal Document AI Assistant")

uploaded_file = st.file_uploader("Upload a scanned legal PDF", type=["pdf"])

if uploaded_file:
    st.success("✅ File uploaded! Running OCR...")

    images = convert_pdf_to_images(uploaded_file)

    all_text = ""
    for img_bytes in images:
        text = run_ocr_on_image(img_bytes)
        all_text += text + "\n\n"

    st.subheader("📃 Extracted Text")
    st.text_area("OCR Output", value=all_text, height=400)
