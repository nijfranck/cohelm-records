# cohelm-takehome

This project is designed to extract text from medical record PDFs and generate responses using OpenAI's GPT models. It's a part of a take-home challenge and serves as a proof-of-concept for the potential applications of AI in medical data processing.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Command Line Options](#command-line-options)
- [Future Improvements](#future-improvements)

## Prerequisites

- Docker
- OpenAI API key

## How to run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/cohelm-takehome.git
```

2. Navigate to the project directory:

```bash
cd cohelm-takehome
```


3. Build the Docker image:

```bash
docker build -t cohelm_records .
```

4. Run the Docker container:

```bash
docker run -it --rm -v $(pwd):/app -e OPENAI_API_KEY=YOUR_OPENAI_API_KEY cohelm_records python main.py /app/dataset --dir
```

Replace `{YOUR_OPENAI_API_KEY}` with your actual OpenAI API key. The `--models` argument is optional and defaults to `gpt-3.5-turbo` if not provided.

## Project Structure

- `main.py`: The main Python script that orchestrates the text extraction from the PDF and the generation of responses using the OpenAI model.
- `utils.py`: Contains utility functions for text extraction from the PDF.
- `queries.py`: contains functions and classes for generating queries to the OpenAI API
- `Dockerfile`: Defines the Docker image for this project.
- `requirements.txt`: Lists the Python dependencies required by this project.

## Command Line Options

The `main.py` script accepts several command-line arguments:

1. `input_path`: (Required) Path to a PDF file or a directory of PDF files.
2. `--dir`: (Optional) Indicates that the `input_path` is a directory.
3. `--models`: (Optional) Specifies one or more OpenAI models to use for generating responses. Defaults to `gpt-3.5-turbo`. If more than one models are provided, many outputs are generated and `gpt-4` uses those responses to generate the best answer.

## Future Improvements

1. **Performance Optimization**: Improve application latency by leveraging state-of-the-art quantized open-source Language Models (LLMs). This could significantly speed up the response time of the application.

2. **Enhanced Medical Analysis**: Incorporate state-of-the-art (SOTA) open-source medical models to provide more accurate and comprehensive answers and evaluations of suggested treatments based on the extracted medical records.

3. **API Development**: Develop an API endpoint using Flask. This would allow other applications or services to use the PDF extraction and response generation capabilities of this application.

4. **Interactive Application**: Create an interactive application using Gradio or Streamlit. This would provide a user-friendly interface for testing the workflow and could be used for demonstrations or presentations.

5. **User Interface for File Upload**: Develop a simple frontend that allows users to upload a medical record PDF and receive the generated answers. This would make the application more accessible to non-technical users.
