import os
import openai
import logging

# Load API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_MSG_MEDICAL = "You are a helpful medical expert assistant"
SYSTEM_MSG_JSON = "You are a helpful JSON parser assistant"
MODEL_NAME = "gpt-3.5-turbo"

def openai_response(text, system_msg):
    """Get a response from the OpenAI API."""

    logging.info("Generating response from OpenAI...")
    try:
        completion = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": text},
            ]
        )
        return completion.choices[0].message.content
    except openai.OpenAIError as e:
        logging.error(f"Failed to get response from OpenAI: {e}")
        return None