from app.agents.ingestor import ingestion_node


state = {
    "research_id": "test-research-001",
    "documents": [
        {
            "title": "Test AI Document",
            "url": "https://example.com/ai",
            "query": "artificial intelligence",
            "content": (
                "Artificial intelligence enables machines to perform tasks that normally "
                "require human intelligence. Machine learning is a major approach used in "
                "AI systems. Deep learning uses neural networks with multiple layers to "
                "learn complex patterns from large datasets. Natural language processing "
                "allows machines to understand and generate human language.\n\n"

                "AI Agents\n"
                "AI agents extend these capabilities by using models, tools, memory, "
                "and reasoning to perform multi-step tasks. Unlike simple chatbots, "
                "agents can select tools, retrieve information, make decisions, and "
                "execute actions based on a defined objective. This introduces additional "
                "engineering and operational complexity.\n\n"

                "Production Challenges\n"
                "Production AI agents must handle reliability, scalability, latency, "
                "security, monitoring, and integration with existing systems. Reliability "
                "is important because agents may produce different outputs for similar "
                "inputs. Scalability becomes important when the number of users and "
                "workflows increases. Latency can affect applications that require fast "
                "responses.\n\n"

                "Security and Monitoring\n"
                "Production agents may interact with sensitive information, external APIs, "
                "databases, and business systems. Security controls are therefore required "
                "to restrict access and prevent unauthorized actions. Monitoring is also "
                "important because agent behavior can change as models, prompts, data, "
                "and external tools change over time.\n\n"

                "System Integration\n"
                "Integrating AI agents with existing enterprise systems can introduce "
                "additional complexity. Organizations may need to connect agents with "
                "databases, APIs, authentication systems, legacy applications, and data "
                "pipelines. These integrations must remain reliable as the surrounding "
                "systems evolve.\n\n"

                "Governance\n"
                "Organizations deploying AI agents may also need governance processes "
                "covering privacy, compliance, auditing, human oversight, and responsibility "
                "for agent actions. These requirements become increasingly important when "
                "agents are allowed to perform consequential actions without direct human "
                "intervention."
            ),
        }
    ]
}

result = ingestion_node(state)

print("Chunks created:", len(result["chunks"]))

for index, chunk in enumerate(result["chunks"]):
    print(f"\n--- Chunk {index} ---")
    print("Length:", len(chunk["content"]))
    print("Content:", chunk["content"])



from app.rag.chunker import clean_text

test_text = (
    "generate human language. "
    "to perform multi-step tasks. "
    "databases, and business systems. "
    "authentication systems. "
    "These requirements are important."
)

print("\n=== CLEAN TEXT TEST ===")
print(clean_text(test_text))