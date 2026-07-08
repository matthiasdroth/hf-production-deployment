import logging

from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

from app.inference import predict_sentiment
from app.schemas import PredictionRequest, PredictionResponse


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    except Exception as error:
        logger.exception(error)
        raise HTTPException(status_code=500, detail="Prediction failed.")
