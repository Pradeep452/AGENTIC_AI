from duckduckgo_search import DDGS

def web_search(query: str):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=1))
    return results[0]["body"] if results else "No result found"
