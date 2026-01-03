import google.generativeai as genai
from pypdf import PdfReader
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def read_pdf(path: str) -> str:
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def gemini_document_qa(document_text: str, question: str):
    prompt = f"""
Answer the question ONLY using the document below.
If not present, respond with NOT_IN_DOCUMENT.

DOCUMENT:
{document_text}

QUESTION:
{question}
"""
    response = model.generate_content(prompt)
    answer = response.text.strip()

    if "NOT_IN_DOCUMENT" in answer:
        return None

    return answer
