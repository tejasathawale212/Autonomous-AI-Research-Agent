from app.rag.vector_store import create_collection, COLLECTION_NAME, client


create_collection()

collections = client.get_collections().collections

print("Collection exists:", any(
    collection.name == COLLECTION_NAME
    for collection in collections
))