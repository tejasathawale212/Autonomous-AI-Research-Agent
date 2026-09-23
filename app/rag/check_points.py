from app.rag.vector_store import client, COLLECTION_NAME


points, _ = client.scroll(
    collection_name=COLLECTION_NAME,
    limit=10,
    with_payload=True,
)

for point in points:
    print(
        point.id,
        "|",
        point.payload.get("chunk_id"),
        "|",
        point.payload.get("title"),
    )