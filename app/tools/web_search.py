from tavily import TavilyClient

from app.config import TAVILY_API_KEY


client = TavilyClient(api_key=TAVILY_API_KEY)


def search_web(query: str) -> list[dict]:
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5,
    )

    return response["results"]