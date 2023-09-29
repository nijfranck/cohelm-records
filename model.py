import os
import openai
import logging
from queries import generate_eval_query

# Load API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_MSG_MEDICAL = "You are a helpful medical expert assistant"
SYSTEM_MSG_JSON = "You are a helpful JSON parser assistant"
MODEL_NAME = "gpt-3.5-turbo"

def openai_response(text, system_msg, model_name=MODEL_NAME):
    """Get a response from the OpenAI API."""

    logging.info("Generating response from OpenAI...")
    try:
        completion = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": text},
            ]
        )
        return completion.choices[0].message.content
    except openai.OpenAIError as e:
        logging.error(f"Failed to get response from OpenAI: {e}")
        return None

def evaluate_model(medical_record_query, models):
    """Evaluate the model and return the response."""
    responses = []
    if len(models) > 1:  # If more than one model is provided, use ensemble evaluation
        for model in models:
            logging.info(f"Generating response from OpenAI model {model}...")
            response = openai_response(medical_record_query, SYSTEM_MSG_MEDICAL, model_name=model)
            logging.info(f"Response from OpenAI: {response}")
            if response:
                responses.append(response)
        evaluation_query = generate_eval_query(medical_record_query, models, responses)
        return openai_response(evaluation_query, SYSTEM_MSG_MEDICAL, model_name="gpt-4")
    else:  # If only one model is provided, use it as the default model
        logging.info(f"Generating response from OpenAI model {models[0]}...")
        return openai_response(medical_record_query, SYSTEM_MSG_MEDICAL, model_name=models[0])


    