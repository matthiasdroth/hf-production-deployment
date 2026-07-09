from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

classifier = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer,
)
