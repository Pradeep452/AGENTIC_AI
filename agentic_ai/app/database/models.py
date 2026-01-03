from sqlalchemy import Column, Integer, String, Date
from app.database.db import Base

class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(Date)
    weather_status = Column(String)
