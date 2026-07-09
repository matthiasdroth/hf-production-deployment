# Getting Started

## 1. Prerequisites

Make sure the following software is installed:

- Git
- Docker Desktop

Start Docker Desktop before continuing.

---

## 2. Clone the Repository

```bash
git clone https://github.com/matthiasdroth/hf-production-deployment.git
```

---

## 3. Change into the Project Directory

```bash
cd hf-production-deployment
```

---

## 4. Build the Docker Image

```bash
docker build -t hf-production-deployment .
```

The first build may take several minutes because Docker needs to download the Python base image and the required Python packages.

---

## 5. Run the Application

```bash
docker run -p 8000:8000 hf-production-deployment
```

Once the application has started successfully, you should see output similar to:

```text
INFO:     Started server process ...
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

Leave this terminal open while using the application.

---

# Using the Application

## Browser-based User Interface

Open your browser and navigate to

```
http://127.0.0.1:8000/ui
```

Enter a sentence, for example

```
I am happy.
```

Click **Analyze Sentiment**.

The application returns one of the following sentiment classes:

- POSITIVE
- NEUTRAL
- NEGATIVE

Example inputs:

| Input | Expected Output |
|--------|-----------------|
| I am happy. | POSITIVE |
| 4+4=8. | NEUTRAL |
| I am sad. | NEGATIVE |

---

## REST API

You can also access the application programmatically.

Example request:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"4+4=8."}'
```

Example response:

```json
{
  "label": "NEUTRAL",
  "score": 0.789
}
```

---

## Swagger Documentation

FastAPI automatically provides interactive API documentation.

Open

```
http://127.0.0.1:8000/docs
```

You can interactively test all API endpoints directly from your browser.

---

## ReDoc Documentation

Alternatively, open

```
http://127.0.0.1:8000/redoc
```

for a more documentation-oriented view of the API.

---

## Stopping the Application

Return to the terminal running Docker and press

```text
Ctrl + C
```

or stop the container from another terminal:

```bash
docker ps
docker stop <CONTAINER_ID>
```
