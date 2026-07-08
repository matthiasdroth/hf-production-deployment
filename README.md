# HuggingFace AI Production Deployment

## Setup and Run Instructions

Follow these steps to run the application locally.

### 1. Clone the repository

``` bash
git clone https://github.com/matthiasdroth/hf-production-deployment.git
```

### 2. Enter the project directory

``` bash
cd hf-production-deployment
```

### 3. Create a virtual environment

``` bash
python3 -m venv env
```

### 4. Activate the virtual environment

``` bash
source env/bin/activate
```

### 5. Install the dependencies

``` bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 6. Start the FastAPI application

``` bash
uvicorn app.main:app --reload
```

The server should start on:

    http://127.0.0.1:8000

## Testing the Application

### 7. Verify that the API is running

Open:

    http://127.0.0.1:8000/

Expected response:

``` json
{
  "application": "Production HuggingFace Model API",
  "status": "running"
}
```

### 8. Open the web interface

Navigate to:

    http://127.0.0.1:8000/ui

Enter some text, click **Predict**, and verify that the prediction is
displayed.

### 9. Test the API directly

``` bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"I love machine learning."}'
```

Example response:

``` json
{
  "label": "POSITIVE",
  "score": 0.99
}
```

### 10. Run the automated tests

``` bash
python -m pytest
```

### 11. Stop the server

Press:

    Ctrl + C

## Project Structure

``` text
hf-production-deployment/
├── app/
├── tests/
├── Images/
├── requirements.txt
├── README.md
├── Dockerfile
├── .dockerignore
└── .gitignore
```

## Notes

-   Always activate the virtual environment before running the
    application.
-   If port 8000 is already in use, stop the previous Uvicorn process or
    choose another port.
-   The web interface is available at `/ui`, while `/predict` provides
    the JSON API.
