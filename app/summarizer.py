
from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")

def summarize_text(text, summary_type="quick"):
    max_len = 130 if summary_type == "quick" else 300
    result = summarizer(text[:1000], max_length=max_len, min_length=30, do_sample=False)
    return result[0]['summary_text']
