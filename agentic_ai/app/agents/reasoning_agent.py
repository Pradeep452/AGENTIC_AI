def reasoning_agent(query: str) -> str:
    q = query.lower()

    if "weather" in q:
        return "WEATHER"

    if "policy" in q or "document" in q or "resume" in q:
        return "DOCUMENT"

    if "schedule" in q:
        return "MEETING"

    if "meeting" in q:
        return "DATABASE"

    return "UNKNOWN"
