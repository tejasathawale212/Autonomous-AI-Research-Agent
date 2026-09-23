from app.agents.graph import build_research_graph
import uuid

graph = build_research_graph()

result = graph.invoke(
    {
        "research_id": str(uuid.uuid4()),
        "question": "What are the major challenges of deploying AI agents in production?",
        "objective": "",
        "sub_questions": [],
        "search_queries": [],
        "sources": [],
        "documents": [],
        "chunks": [],
        "retrieved_context": [],
        "findings": [],
        "final_report": "",
        "evidence_sufficient": False,
        "research_iterations": 0,
        "max_iterations": 2,
    }
)

print("\n=== RESEARCH SUMMARY ===")

print(f"Research ID: {result['research_id']}")
print(f"Question: {result['question']}")
print(f"Sources: {len(result['sources'])}")
print(f"Documents: {len(result['documents'])}")
print(f"Chunks: {len(result['chunks'])}")
print(f"Retrieved Context: {len(result['retrieved_context'])}")
print(f"Evidence Sufficient: {result['evidence_sufficient']}")
print(f"Research Iterations: {result['research_iterations']}")

print("\n=== FINAL REPORT ===\n")
print(result["final_report"])