from app.rag.retriever import retrieve_relevant_chunks


query = "What is artificial intelligence?"

results = retrieve_relevant_chunks(
    query,
    limit=3,
)

print("Results:", len(results))

for result in results:
    print("\nScore:", round(result["score"], 4))
    print("Title:", result["title"])
    print("URL:", result["url"])
    print("Content:", result["content"][:150])