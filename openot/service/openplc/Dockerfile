# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Download and install OpenPLC
RUN wget https://github.com/thiagoralves/OpenPLC_v3/archive/refs/heads/master.zip -O openplc.zip \
    && unzip openplc.zip \
    && rm openplc.zip \
    && mv OpenPLC_v3-master OpenPLC_v3

# Set the working directory to OpenPLC
WORKDIR /usr/src/app/OpenPLC_v3

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port OpenPLC runs on
EXPOSE 8080

# Run OpenPLC
CMD ["python", "start_openplc.py"]