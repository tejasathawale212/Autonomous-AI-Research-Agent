from uuid import NAMESPACE_URL, uuid5

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PayloadSchemaType,
    PointStruct,
    VectorParams,
)

from app.config import QDRANT_URL, QDRANT_API_KEY



client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    timeout=60,
)





COLLECTION_NAME = "research_chunks"
VECTOR_SIZE = 384


def create_collection() -> None:
    collections = client.get_collections().collections
    existing_names = {collection.name for collection in collections}

    if COLLECTION_NAME not in existing_names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )

    client.create_payload_index(
        collection_name=COLLECTION_NAME,
        field_name="research_id",
        field_schema=PayloadSchemaType.KEYWORD,
    )


def upsert_chunks(
        chunks: list[dict],
        embeddings: list[list[float]],
    ) -> None:
    if len(chunks) != len(embeddings):
        raise ValueError("Number of chunks must match number of embeddings")

    points = []

    for chunk, embedding in zip(chunks, embeddings):
        points.append(
            PointStruct(
                id=str(
                    uuid5(
                        NAMESPACE_URL,
                        f"{chunk['research_id']}:{chunk['chunk_id']}",
                    )
                ),
                vector=embedding,
                payload={
                    "research_id": chunk["research_id"],
                    "chunk_id": chunk["chunk_id"],
                    "document_index": chunk["document_index"],
                    "chunk_index": chunk["chunk_index"],
                    "title": chunk["title"],
                    "url": chunk["url"],
                    "query": chunk["query"],
                    "content": chunk["content"],
                },
            )
        )

    BATCH_SIZE = 20

    for start in range(0, len(points), BATCH_SIZE):
        batch = points[start:start + BATCH_SIZE]

        client.upsert(
            collection_name=COLLECTION_NAME,
            points=batch,
        )

def search_chunks(
    query_vector: list[float],
    research_id: str,
    limit: int = 5,
) -> list[dict]:
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        query_filter={
            "must": [
                {
                    "key": "research_id",
                    "match": {
                        "value": research_id,
                    },
                }
            ]
        },
        limit=limit,
        with_payload=True,
    ).points

    return [
        {
            "score": point.score,
            **point.payload,
        }
        for point in results
    ]


def count_chunks() -> int:
    return client.count(
        collection_name=COLLECTION_NAME,
        exact=True,
    ).count


def delete_collection() -> None:
    client.delete_collection(COLLECTION_NAME)