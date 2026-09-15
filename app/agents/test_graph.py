from app.agents.graph import build_research_graph


graph = build_research_graph()

result = graph.invoke(
    {
        "question": "What are the major challenges of deploying AI agents in production?",
        "objective": "",
        "research_plan": [],
        "search_queries": [],
        "sources": [],
        "documents": [],
        "chunks": [],
        "retrieved_context": [],
        "findings": [],
        "final_report": "",
    }
)

print(result)