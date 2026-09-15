from app.services.llm import ask_llm
from app.tools.web_scraper import extract_webpage
from app.tools.web_search import search_web


def research(query: str) -> str:
    search_results = search_web(query)

    source_contents = []

    for result in search_results[:3]:
        content = extract_webpage(result["url"])

        source_contents.append(
            f"Source: {result['title']}\n"
            f"URL: {result['url']}\n"
            f"Content:\n{content}"
        )

    sources = "\n\n".join(source_contents)

    prompt = f"""
    You are an AI research assistant.

    Research question:
    {query}

    Here is the content collected from web sources:

    {sources}

    Analyze the sources and provide a clear, accurate answer to the
    research question. Base your answer on the provided source content.
    """

    return ask_llm(prompt)