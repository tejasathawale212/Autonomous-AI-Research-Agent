
from app.agents.state import ResearchState
from app.rag.chunker import chunk_documents
from app.rag.embeddings import generate_embeddings
from app.rag.vector_store import create_collection, upsert_chunks


def ingestion_node(state: ResearchState) -> dict:
    chunks = chunk_documents(state["documents"])

    for chunk in chunks:
        chunk["research_id"] = state["research_id"]

    print(f"Ingestion: {len(chunks)} chunks")

    embeddings = generate_embeddings(
        [chunk["content"] for chunk in chunks]
    )

    create_collection()
    upsert_chunks(chunks, embeddings)

    return {
        "chunks": chunks,
    }