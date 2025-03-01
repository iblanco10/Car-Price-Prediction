# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /opt/program

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip before installing dependencies
RUN pip install --upgrade pip

# Copy requirements file first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the model directory exists before copying the model
RUN mkdir -p /opt/ml/model /opt/ml/input/data

# Copy the trained model explicitly
COPY car_price_model.pkl /opt/ml/model/model.pkl

# Copy all application files to /opt/program
COPY . /opt/program/

# Debugging: List files in /opt/program/ to verify contents
RUN ls -l /opt/program/
RUN ls -l /opt/ml/model/

# Ensure the correct working directory
WORKDIR /opt/program

# Run the model serving script
ENTRYPOINT ["python", "serve.py"]
