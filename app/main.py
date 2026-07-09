from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from prometheus_fastapi_instrumentator import Instrumentator

from app.inference import predict_sentiment
from app.schemas import PredictionRequest, PredictionResponse

app = FastAPI(title="Production HuggingFace Model API")

Instrumentator().instrument(app).expose(app)


@app.get("/")
def root():
    return {
        "application": "Production HuggingFace Model API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        return predict_sentiment(request.text)
    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed.")


@app.get("/ui", response_class=HTMLResponse)
def ui():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hugging Face Sentiment API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 40px auto;
                padding: 20px;
                line-height: 1.6;
            }

            textarea {
                width: 100%;
                font-size: 16px;
                padding: 10px;
            }

            button {
                margin-top: 12px;
                padding: 10px 18px;
                font-size: 16px;
                cursor: pointer;
            }

            pre {
                background: #f4f4f4;
                padding: 16px;
                border-radius: 6px;
            }
        </style>
    </head>
    <body>
        <h1>Hugging Face Sentiment Analysis</h1>

        <p>Enter a sentence and let the API classify its sentiment.</p>

        <textarea id="text" rows="5">I love machine learning.</textarea>
        <br>

        <button onclick="predict()">Predict</button>

        <h2>Result</h2>
        <pre id="result">No prediction yet.</pre>

        <script>
            async function predict() {
                const text = document.getElementById("text").value;

                const response = await fetch("/predict", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ text: text })
                });

                const data = await response.json();

                document.getElementById("result").textContent =
                    JSON.stringify(data, null, 2);
            }
        </script>
    </body>
    </html>
    """