# Hugging Face Production Deployment

A production-style sentiment analysis application built with **FastAPI**, **Docker**, and **Hugging Face Transformers**.

The application exposes both a **REST API** and a **browser-based web interface** for classifying English text into **Positive**, **Neutral**, and **Negative** sentiment.

The project demonstrates how to deploy a Hugging Face Transformer model as a production-ready web service using modern MLOps practices such as containerization, automated testing, and API documentation.

---

# Features

- FastAPI REST API
- Browser-based web interface
- Three-class sentiment analysis (Positive / Neutral / Negative)
- Hugging Face Transformers
- Dockerized deployment
- Interactive Swagger / OpenAPI documentation
- Automated tests with pytest
- Production-ready project structure

---

# Project Structure

```
hf-production-deployment/
│
├── app/
│   ├── __init__.py
│   ├── inference.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── tests/
│   └── test_api.py
│
├── Dockerfile
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Prerequisites

- Docker Desktop
- Git

Clone the repository

```bash
git clone https://github.com/matthiasdroth/hf-production-deployment.git
cd hf-production-deployment
```

---

# Build the Docker Image

```bash
docker build -t hf-production-deployment .
```

---

# Run the Application

```bash
docker run -p 8000:8000 hf-production-deployment
```

Once the container has started successfully, you should see

```
INFO:     Started server process ...
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

# Application Endpoints

## Root API Status

```
GET /
```

Example response

```json
{
  "application": "Production Hugging Face Model API",
  "status": "running"
}
```

---

## Web Interface

Open

```
http://127.0.0.1:8000/ui
```

The web interface allows users to enter arbitrary text and classify its sentiment interactively.

---

## Prediction API

```
POST /predict
```

Example request

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"I am happy."}'
```

Example response

```json
{
  "label": "POSITIVE",
  "score": 0.969
}
```

Another example

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"4+4=8."}'
```

Example response

```json
{
  "label": "NEUTRAL",
  "score": 0.789
}
```

---

# Interactive API Documentation

FastAPI automatically generates interactive OpenAPI documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

The Swagger UI allows users to interactively test all API endpoints directly from their browser.

---

# Running the Tests

Run the automated test suite

```bash
python -m pytest tests/test_api.py -v
```

Expected output

```
============================= test session starts =============================

...

============================== 3 passed ==============================
```

---

# Sentiment Model

This application uses the Hugging Face model

```
cardiffnlp/twitter-roberta-base-sentiment-latest
```

The model predicts one of three sentiment classes:

- NEGATIVE
- NEUTRAL
- POSITIVE

Unlike binary sentiment models, this model correctly distinguishes neutral factual statements from genuinely positive or negative sentiment.

Example predictions

| Input       | Prediction |
| ----------- | ---------- |
| I am happy. | POSITIVE   |
| 4+4=8.      | NEUTRAL    |
| I am sad.   | NEGATIVE   |

---

# Technology Stack

- Python
- FastAPI
- Uvicorn
- Docker
- Hugging Face Transformers
- PyTorch
- Pydantic
- pytest
- Swagger / OpenAPI

---

# Architecture

```
                Browser
                   │
                   ▼
         FastAPI Web Application
         ┌───────────────────────┐
         │                       │
         │  GET  /               │
         │  GET  /ui             │
         │  POST /predict        │
         │  GET  /health         │
         │  GET  /docs           │
         └───────────────────────┘
                   │
                   ▼
        Hugging Face Transformers
                   │
                   ▼
      RoBERTa Sentiment Classification
                   │
                   ▼
      POSITIVE / NEUTRAL / NEGATIVE
```

---

# Future Improvements

Possible future extensions include

- GitHub Actions CI/CD
- Kubernetes deployment
- Environment-based model configuration
- Model versioning
- Prometheus monitoring
- Authentication
- GPU inference support
- Benchmarking and load testing

---

# License

This project is licensed under the MIT License.
