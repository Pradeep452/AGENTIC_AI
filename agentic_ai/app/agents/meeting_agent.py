from app.tools.weather_tool import fetch_weather
from app.database.db import SessionLocal
from app.database.models import Meeting

def meeting_agent(city, meeting_date):
    weather = fetch_weather(city, meeting_date.isoformat())

    if "rain" in weather["description"].lower():
        return "Bad weather. Meeting not scheduled."

    db = SessionLocal()
    existing = db.query(Meeting).filter(Meeting.date == meeting_date).first()

    if existing:
        return "Meeting already scheduled."

    meeting = Meeting(
        title="Team Meeting",
        date=meeting_date,
        weather_status="Good"
    )

    db.add(meeting)
    db.commit()

    return "Meeting scheduled successfully."
