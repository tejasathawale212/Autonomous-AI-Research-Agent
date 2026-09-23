from app.agents.state import ResearchState
from app.rag.retriever import retrieve_relevant_chunks


def retriever_node(state: ResearchState) -> dict:
    queries = [state["question"], *state["sub_questions"]]

    retrieved_context = []
    seen_chunks = set()

    for query in queries:
        results = retrieve_relevant_chunks(
            query,
            research_id=state["research_id"],
            limit=2,
        )

        for result in results:
            chunk_id = result["chunk_id"]

            if chunk_id not in seen_chunks:
                seen_chunks.add(chunk_id)
                retrieved_context.append(result)

    return {
        "retrieved_context": retrieved_context[:6]
    }