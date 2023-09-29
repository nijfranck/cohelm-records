import os
import logging
import pytesseract
from pdf2image import convert_from_path


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""

    logging.info("Extracting text from PDF...")
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"No file found at {pdf_path}")
    pages = convert_from_path(pdf_path, 500)
    return ''.join(pytesseract.image_to_string(page, lang='eng') + '\n' for page in pages)
