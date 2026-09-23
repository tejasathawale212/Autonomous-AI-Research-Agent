from app.agents.state import ResearchState
from app.tools.web_scraper import extract_webpage


def extractor_node(state: ResearchState) -> dict:
    documents = []

    for source in state["sources"]:
        try:
            content = extract_webpage(source["url"])

            documents.append(
                {
                    "title": source["title"],
                    "url": source["url"],
                    "query": source["query"],
                    "content": content,
                }
            )

        except Exception as error:
            print(f"Failed to extract {source['url']}: {error}")

    return {
        "documents": documents,
    }