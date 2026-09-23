from app.agents.evaluator import evaluate_evidence


strong_state = {
    "question": "What are the major challenges of deploying AI agents in production?",
    "retrieved_context": [
        {
            "title": "Production AI Agents",
            "url": "https://example.com/source1",
            "content": (
                "Production AI agents face challenges involving scalability, "
                "latency, monitoring, security, data management, reliability, "
                "and integration with existing systems."
            ),
        },
        {
            "title": "AI Agent Infrastructure",
            "url": "https://example.com/source2",
            "content": (
                "Production deployment requires monitoring, fault tolerance, "
                "security controls, data quality management, and scalable "
                "infrastructure."
            ),
        },
    ],
}


weak_state = {
    "question": "What are the major challenges of deploying AI agents in production?",
    "retrieved_context": [
        {
            "title": "History of Artificial Intelligence",
            "url": "https://example.com/source3",
            "content": (
                "Artificial intelligence began as a field of research "
                "in the twentieth century."
            ),
        },
    ],
}


print("STRONG EVIDENCE:")
print(evaluate_evidence(strong_state))

print("\nWEAK EVIDENCE:")
print(evaluate_evidence(weak_state))