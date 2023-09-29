import json
import logging
from utils import extract_text_from_pdf
from model import openai_response, SYSTEM_MSG_MEDICAL, SYSTEM_MSG_JSON
from queries import generate_medical_record_query, generate_json_query


# Set up logging
logging.basicConfig(level=logging.INFO)

def main():
    """Main application function."""

    text = extract_text_from_pdf('dataset/medical-record.pdf')
    medical_record_query = generate_medical_record_query(text)
    response = openai_response(medical_record_query, SYSTEM_MSG_MEDICAL)
    logging.info(f"Response from OpenAI: {response}")
    if response:
        json_query = generate_json_query(response)
        json_txt = openai_response(json_query, SYSTEM_MSG_JSON)
        try:
            json_output = json.loads(json_txt)
            logging.info(f"JSON output: {json_output}")
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse JSON: {e}")

if __name__ == "__main__":
    main()
