from app.tools.weather_tool import fetch_weather

def weather_agent(city: str, date: str):
    weather = fetch_weather(city, date)
    return {
        "agent": "Weather Intelligence Agent",
        "city": city,
        "date": date,
        "weather": weather
    }
