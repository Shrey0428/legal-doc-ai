import os
import fitz  # PyMuPDF
from google.cloud import vision
from PIL import Image

def convert_pdf_to_images(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    images = []
    for page in doc:
        pix = page.get_pixmap(dpi=300)
        img_bytes = pix.tobytes("png")
        images.append(img_bytes)
    return images

def run_ocr_on_image(image_bytes, credentials_path="legal-ocr-project-02eb8bdcb492.json"):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=image_bytes)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if not texts:
        return ""
    return texts[0].description

