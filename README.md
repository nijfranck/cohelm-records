# cohelm-takehome

This project is a take-home challenge to produce answers from a medical record PDF. It uses OpenAI's GPT models to generate responses based on the extracted text from the PDF.

## Prerequisites

- Docker
- OpenAI API key

## How to run

1. Build the Docker image:

bash
`docker build -t cohelm_records .`

2. Run the Docker container:

`docker run -it --rm -v $(pwd):/app -e OPENAI_API_KEY=YOUR_OPENAI_API_KEY cohelm_records python main.py /app/dataset --dir`

Replace `{YOUR_OPENAI_API_KEY}` with your actual OpenAI API key. The `--models` argument is optional and defaults to `gpt-3.5-turbo` if not provided.

## Project Structure

- `main.py`: The main Python script that orchestrates the text extraction from the PDF and the generation of responses using the OpenAI model.
- `utils.py`: Contains utility functions for text extraction from the PDF.
- `Dockerfile`: Defines the Docker image for this project.
- `requirements.txt`: Lists the Python dependencies required by this project.


## Options

The main.py script in your application accepts several command-line arguments that allow you to customize its behavior:

1. input_path: This is a positional argument, meaning it's required. You should provide the path to a PDF file or a directory of PDF files that you want to process.

2. --dir: This is an optional argument. If provided, it indicates that the input_path is a directory. If not provided, the script will assume that input_path is a single PDF file.

3. --models: This is an optional argument. It allows you to specify one or more OpenAI models to use for generating responses. If more than one model is provided, we perform an ensemble model run where a GPT-4 model will evaluate the resulting responses. The models should be provided as a space-separated list. If not provided, the script will use the gpt-3.5-turbo model by default.