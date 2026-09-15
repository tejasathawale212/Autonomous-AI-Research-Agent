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

def search_multiple_queries(
        queries: list[str],
        max_queries: int = 3,
        results_per_query: int = 3,
    ) -> list[dict]:
    unique_queries = list(dict.fromkeys(queries))[:max_queries]

    collected_sources = []
    seen_urls = set()

    for query in unique_queries:
        results = search_web(query)

        for result in results[:results_per_query]:
            url = result.get("url")

            if not url or url in seen_urls:
                continue

            seen_urls.add(url)

            collected_sources.append(
                {
                    "title": result.get("title", ""),
                    "url": url,
                    "content": result.get("content", ""),
                    "query": query,
                }
            )

    return collected_sources