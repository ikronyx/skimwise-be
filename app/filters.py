
from textblob import TextBlob

def apply_filters(summary: str, filter_type: str):
    if filter_type == "sentiment":
        blob = TextBlob(summary)
        return {"polarity": blob.sentiment.polarity, "summary": summary}
    return {"summary": summary}
