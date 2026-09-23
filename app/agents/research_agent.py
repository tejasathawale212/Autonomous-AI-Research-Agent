from app.agents.graph import build_research_graph


def research(query: str):
    graph = build_research_graph()

    initial_state = {
        "research_id": "research_001",
        "question": query,
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
        "is_research_question": False,
    }

    result = graph.invoke(initial_state)

    return {
        "final_report": result["final_report"],
        "sources": result["sources"],
    }