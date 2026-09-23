from app.agents.query_refiner import query_refiner_node


state = {
    "question": "What are the major challenges of deploying AI agents in production?",
    "retrieved_context": [
        {
            "title": "AI Agent Production Challenges",
            "content": (
                "AI agents face scalability and latency challenges when "
                "deployed in production. Large workloads can increase "
                "response times and infrastructure requirements."
            ),
        },
        {
            "title": "AI Agent Deployment",
            "content": (
                "Production systems require scalable infrastructure and "
                "performance optimization."
            ),
        },
    ],
    "research_iterations": 0,
}


result = query_refiner_node(state)

print("\nREFINED SEARCH QUERIES:\n")

for query in result["search_queries"]:
    print("-", query)

print("\nRESEARCH ITERATIONS:")
print(result["research_iterations"])