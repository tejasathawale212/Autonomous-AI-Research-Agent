from app.agents.synthesizer import synthesizer_node


state = {
    "question": "What are the major challenges of deploying AI agents in production?",
    "retrieved_context": [
        {
            "title": "AI Agent Production Challenges",
            "url": "https://example.com/source1",
            "content": (
                "AI agents deployed in production can face scalability, "
                "latency, reliability, monitoring, security, and integration "
                "challenges."
            ),
        },
        {
            "title": "AI Agent Security",
            "url": "https://example.com/source2",
            "content": (
                "Production AI systems require controls for protecting "
                "sensitive data and managing unauthorized access."
            ),
        },
        {
            "title": "Unrelated AI History",
            "url": "https://example.com/source3",
            "content": (
                "Artificial intelligence research began in the 1950s. "
                "The field later developed machine learning and deep learning."
            ),
        },
    ],
}


result = synthesizer_node(state)

print("\nFINAL REPORT:\n")
print(result["final_report"])