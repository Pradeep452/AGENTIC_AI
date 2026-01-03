from datetime import date, timedelta

def parse_date(text: str):
    text = text.lower()
    if "tomorrow" in text:
        return date.today() + timedelta(days=1)
    return date.today()
