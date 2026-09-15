from app.agents.state import ResearchState
from app.tools.web_search import search_multiple_queries


def search_node(state: ResearchState) -> dict:
    sources = search_multiple_queries(
        state["search_queries"],
        max_queries=3,
        results_per_query=3,
    )

    return {
        "sources": sources,
    }