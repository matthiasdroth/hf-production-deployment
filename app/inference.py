from transformers import pipeline
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)
def predict_sentiment(text: str) -> dict:
    result = classifier(text)[0]
    return {
        "label": result["label"],
        "score": float(result["score"]),
    }
