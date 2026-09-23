from app.rag.embeddings import generate_embeddings
from app.rag.vector_store import search_chunks


def retrieve_relevant_chunks(
        query: str,
        research_id: str,
        limit: int = 5,
    ) -> list[dict]:
    query_embedding = generate_embeddings([query])[0]

    return search_chunks(
        query_vector=query_embedding,
        research_id=research_id,
        limit=limit,
    )