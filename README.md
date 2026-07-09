# Hugging Face Production Deployment

A production-style sentiment analysis application built with FastAPI, Docker, and Hugging Face Transformers.

The application exposes both a REST API and a browser-based web interface for classifying English text into Positive, Neutral, and Negative sentiment.

## Features

- FastAPI REST API
- Browser-based web interface
- Three-class sentiment analysis
- Hugging Face Transformers
- Dockerized deployment
- Swagger / OpenAPI documentation
- Automated tests with pytest

## Run with Docker

Build the image:

```bash
docker build -t hf-production-deployment .
```

Run the container:

```bash
docker run -p 8000:8000 hf-production-deployment
```

Open the web interface:

```text
http://127.0.0.1:8000/ui
```

Open Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Test the API

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"4+4=8."}'
```

Expected label:

```text
NEUTRAL
```

## Run tests

```bash
python -m pytest tests/test_api.py -v
```

## Model

This application uses:

```text
cardiffnlp/twitter-roberta-base-sentiment-latest
```

It predicts:

- NEGATIVE
- NEUTRAL
- POSITIVE
