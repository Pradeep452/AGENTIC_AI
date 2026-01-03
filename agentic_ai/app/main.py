from fastapi import FastAPI, UploadFile, File
import shutil
import os
import re

from app.agents.reasoning_agent import reasoning_agent
from app.agents.weather_agent import weather_agent
from app.agents.document_agent import document_agent
from app.agents.meeting_agent import meeting_agent
from app.agents.nl_to_db_agent import nl_to_db_agent
from app.tools.document_tool import read_pdf
from app.utils.date_parser import parse_date

app = FastAPI(title="Agentic AI Backend")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

DOCUMENT_TEXT = ""


# ---------------- UTILITY ----------------
def extract_city(question: str) -> str:
    """
    Extract city from user question.
    """
    match = re.search(r"in\s+([a-zA-Z\s]+)", question.lower())
    if match:
        return match.group(1).strip().title()
    return None


# ---------------- ROOT ----------------
@app.get("/")
def root():
    return {
        "status": "Agentic AI Backend Running",
        "docs": "/docs"
    }


# ---------------- DOCUMENT UPLOAD ----------------
@app.post("/document/upload")
def upload_document(file: UploadFile = File(...)):
    global DOCUMENT_TEXT

    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text = read_pdf(path)

    if not text or not text.strip():
        DOCUMENT_TEXT = ""
        return {"error": "No readable text found in document"}

    DOCUMENT_TEXT = text.strip()

    return {
        "message": "Document uploaded successfully",
        "characters": len(DOCUMENT_TEXT)
    }


# ---------------- AGENT 1: WEATHER ----------------
@app.post("/weather")
def weather_endpoint(question: str):
    """
    User asks:
    - What is the weather in Chennai?
    - Weather in Bengaluru tomorrow
    """
    city = extract_city(question)
    date = parse_date(question).isoformat()

    return weather_agent(city, date)


# ---------------- AGENT 2: DOCUMENT + WEB ----------------
@app.post("/document/query")
def document_query(question: str):
    """
    1) Answer from document
    2) If NOT in document → Web search
    """
    if not DOCUMENT_TEXT:
        return {"answer": "No document uploaded"}

    response = document_agent(question, DOCUMENT_TEXT)

    if not response or any(
        x in str(response).lower()
        for x in ["not found", "not mentioned", "no information"]
    ):
        return {
            "source": "web",
            "answer": response
        }

    return {
        "source": "document",
        "answer": response
    }


# ---------------- AGENT 3: MEETING + WEATHER ----------------
@app.post("/meeting")
def meeting_weather_logic(question: str):
    city = extract_city(question)
    date = parse_date(question)

    if not date:
        return {"error": "Unable to understand date from question"}

    # 1️⃣ Always run weather agent
    try:
        weather = weather_agent(city, date.isoformat())
    except Exception as e:
        return {
            "error": "Weather service failed",
            "details": str(e)
        }

    # 2️⃣ Always run meeting agent (DB logic inside)
    meeting = meeting_agent(city, date)

    # 3️⃣ Reasoning
    if weather.get("condition") == "BAD":
        return {
            "decision": "MEETING_NOT_RECOMMENDED",
            "reason": "Bad weather conditions",
            "city": city,
            "weather": weather,
            "meeting_status": meeting
        }

    return {
        "decision": "MEETING_OK",
        "reason": "Weather is good",
        "city": city,
        "weather": weather,
        "meeting_status": meeting
    }


# ---------------- AGENT 4: NL → DB ----------------
@app.post("/database/query")
def database_query(question: str):
    return nl_to_db_agent(question)


# ---------------- SMART AGENTIC ROUTER ----------------
@app.post("/query")
def smart_query(question: str):
    """
    Agentic AI Flow
    """
    decision = reasoning_agent(question)

    if decision == "WEATHER":
        city = extract_city(question)
        return weather_agent(city, parse_date(question).isoformat())

    if decision == "DOCUMENT":
        return document_query(question)

    if decision == "MEETING":
        return meeting_weather_logic(question)

    if decision == "DATABASE":
        return nl_to_db_agent(question)

    return {"answer": "Unable to process query"}
