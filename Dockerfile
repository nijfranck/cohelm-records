# Use an official Python runtime as a parent image
FROM python:3.10

# Install poppler-utils
RUN apt-get update && apt-get install -y poppler-utils tesseract-ocr

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "main.py"]