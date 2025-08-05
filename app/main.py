
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from app.pdf_parser import extract_text_from_pdf
from app.summarizer import summarize_text
from app.filters import apply_filters

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize-pdf/")
async def summarize_pdf(file: UploadFile = File(...), summary_type: str = Form("quick")):
    text = extract_text_from_pdf(file)
    summary = summarize_text(text, summary_type)
    return {"summary": summary}

@app.post("/summarize-url/")
async def summarize_url(url: str = Form(...), summary_type: str = Form("quick")):
    from newspaper import Article
    article = Article(url)
    article.download()
    article.parse()
    text = article.text
    summary = summarize_text(text, summary_type)
    return {"summary": summary}
