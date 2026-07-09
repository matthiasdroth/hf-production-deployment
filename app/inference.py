from app.models import classifier


def predict_sentiment(text: str) -> dict:
    result = classifier(text)[0]

    return {
        "label": result["label"].upper(),
        "score": float(result["score"]),
    }
