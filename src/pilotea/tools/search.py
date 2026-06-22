from duckduckgo_search import DDGS
from typing import List, Dict

def search_web(query: str, max_results: int = 5) -> List[Dict[str, str]]:
    """
    Search the web using DuckDuckGo.
    Returns a list of dictionaries with 'title', 'href', and 'body'.
    """
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        return list(results)

def format_search_results(results: List[Dict[str, str]]) -> str:
    """Format search results into a clean string for the agent."""
    formatted = ""
    for i, res in enumerate(results, 1):
        formatted += f"{i}. {res['title']}\n   URL: {res['href']}\n   Content: {res['body']}\n\n"
    return formatted
