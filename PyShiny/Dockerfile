FROM python:3.11.4-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY ./setup ./setup
RUN pip3 install -r ./setup/requirements.txt
COPY ./src ./src