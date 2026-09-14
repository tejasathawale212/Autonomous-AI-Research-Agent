from app.services.llm import ask_llm
from app.tools.web_search import search_web


def research(query: str) -> str:
    search_results = search_web(query)

    sources = "\n".join(
        f"- {result['title']}: {result['url']}"
        for result in search_results
    )

    prompt = f"""
    You are an AI research assistant.

    Research question:
    {query}

    Web sources found:
    {sources}

    Based on these sources, explain what information is useful for answering
    the research question.
    """

    return ask_llm(prompt)