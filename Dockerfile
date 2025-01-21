# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Debug: List all files in /app
RUN ls -R /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the ASCII animation
CMD ["python", "TIKTOKEXE.py"]

