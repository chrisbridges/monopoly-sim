# Use an official Python image as the base image.
FROM python:3.9-slim

# Set the working directory inside the container.
WORKDIR /app

# Copy the requirements file and install dependencies.
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . /app

# Specify the default command (adjust if your entrypoint is different).
CMD ["python", "main.py"]