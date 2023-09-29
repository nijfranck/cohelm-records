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


def get_filename(file_path):
    """Get the filename from a file path."""
    return os.path.basename(file_path).split('.')[0]

def get_file_paths(input_path, is_directory):
    """Get a list of file paths."""
    file_paths = []
    if is_directory:
        for filename in os.listdir(input_path):
            if filename.endswith(".pdf"):
                file_paths.append(os.path.join(input_path, filename))
    else:
        file_paths.append(input_path)
    return file_paths
