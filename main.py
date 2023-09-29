import json
import logging
import argparse
import os
from utils import extract_text_from_pdf, get_filename
from model import openai_response, SYSTEM_MSG_MEDICAL, SYSTEM_MSG_JSON
from queries import generate_medical_record_query, generate_json_query


# Set up logging
logging.basicConfig(level=logging.INFO)

def main(input_path, is_directory, models):
    """Main application function."""

    file_paths = []
    if is_directory:
        for filename in os.listdir(input_path):
            if filename.endswith(".pdf"):
                file_paths.append(os.path.join(input_path, filename))
    else:
        file_paths.append(input_path)

    for file_path in file_paths:
        text = extract_text_from_pdf(file_path)
        medical_record_query = generate_medical_record_query(text)
        response = openai_response(medical_record_query, SYSTEM_MSG_MEDICAL)
        logging.info(f"Response from OpenAI: {response}")
        if response:
            json_query = generate_json_query(response)
            json_txt = openai_response(json_query, SYSTEM_MSG_JSON)
            try:
                json_output = json.loads(json_txt)
                logging.info(f"JSON output: {json_output}")
                # Save JSON output to a file
                with open(f"outputs/{get_filename(file_path)}.json", "w") as f:
                    json.dump(json_output, f, indent=4)
            except json.JSONDecodeError as e:
                logging.error(f"Failed to parse JSON: {e}")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate JSON from PDFs")
    parser.add_argument("input_path", help="Path to PDF file or directory of PDF files")
    parser.add_argument("--dir", action="store_true", help="Input path is a directory")
    parser.add_argument('--models', type=str, nargs='+', default=['gpt3.5-turbo'], help='OpenAI models to use')
    args = parser.parse_args()
    main(args.input_path, args.dir, args.models)
