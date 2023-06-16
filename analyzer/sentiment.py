from transformers import pipeline


def sentiment(items: str) -> list:
    model_id = "distilbert-base-uncased-finetuned-sst-2-english"
    sentiment_pipeline = pipeline("sentiment-analysis", model=model_id)
    return sentiment_pipeline(items)
