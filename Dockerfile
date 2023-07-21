# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install project dependencies
RUN pip install  -r requirements.txt

# Copy the entire repository to the container's working directory
COPY . .

# Expose the port that Streamlit uses (default is 8501)
EXPOSE 8501

# Run the Streamlit app when the container starts
CMD ["streamlit", "run", "app.py"]
