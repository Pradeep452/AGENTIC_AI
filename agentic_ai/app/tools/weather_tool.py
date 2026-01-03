import requests
from datetime import datetime
from app.config import OPENWEATHER_API_KEY

def fetch_weather(city: str, date: str):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    data = requests.get(url, params=params).json()
    target_date = datetime.strptime(date, "%Y-%m-%d").date()

    for entry in data["list"]:
        entry_date = datetime.fromtimestamp(entry["dt"]).date()
        if entry_date == target_date:
            return {
                "temperature": entry["main"]["temp"],
                "description": entry["weather"][0]["description"]
            }

    return {"description": "No data"}
