from datetime import date, timedelta
from app.database.db import SessionLocal
from app.database.models import Meeting

def nl_to_db_agent(query: str):
    db = SessionLocal()
    q = query.lower()

    if "today" in q:
        meetings = db.query(Meeting).filter(Meeting.date == date.today()).all()

    elif "tomorrow" in q:
        meetings = db.query(Meeting).filter(
            Meeting.date == date.today() + timedelta(days=1)
        ).all()
    else:
        return "Query not understood"

    return [m.title for m in meetings]
