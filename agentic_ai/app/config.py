import os
from dotenv import load_dotenv

load_dotenv()

# OpenWeather API Key
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not OPENWEATHER_API_KEY:
    raise ValueError("OPENWEATHER_API_KEY not found in .env")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")
