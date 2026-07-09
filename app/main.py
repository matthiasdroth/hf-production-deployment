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
        <title>Sentiment Analyzer</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f5f7fa;
                margin: 0;
                padding: 40px;
            }

            .container {
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
            }

            textarea {
                width: 100%;
                height: 140px;
                padding: 12px;
                font-size: 16px;
                box-sizing: border-box;
            }

            button {
                margin-top: 16px;
                padding: 12px 20px;
                font-size: 16px;
                cursor: pointer;
            }

            .result {
                margin-top: 24px;
                padding: 16px;
                background: #f0f3f8;
                border-radius: 8px;
                font-family: monospace;
                white-space: pre-wrap;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hugging Face Sentiment Analyzer</h1>
            <p>Enter text and call the FastAPI-based AI inference API.</p>

            <textarea id="text">I am happy.</textarea>

            <button onclick="predict()">Analyze Sentiment</button>

            <div class="result" id="result">No prediction yet.</div>
        </div>

        <script>
            async function predict() {
                const text = document.getElementById("text").value;
                const resultBox = document.getElementById("result");

                resultBox.textContent = "Analyzing...";

                const response = await fetch("/predict", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ text: text })
                });

                const data = await response.json();

                resultBox.textContent =
                    "Label: " + data.label + "\\n" +
                    "Score: " + data.score.toFixed(4);
            }
        </script>
    </body>
    </html>
    """