from app.database.db import SessionLocal

def get_db():
    return SessionLocal()
