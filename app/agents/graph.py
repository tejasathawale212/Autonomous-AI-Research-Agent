from langgraph.graph import END, START, StateGraph

from app.agents.extractor import extractor_node
from app.agents.ingestor import ingestion_node
from app.agents.planner import planner_node
from app.agents.searcher import search_node
from app.agents.state import ResearchState
from app.agents.retriever import retriever_node
from app.agents.evaluator import evaluate_evidence
from app.agents.synthesizer import synthesizer_node
from app.agents.query_refiner import query_refiner_node
from app.agents.question_validator import validate_question

def route_after_validator(state: ResearchState) -> str:
    if state["is_research_question"]:
        return "planner"

    return "end"

def non_research_response(state: ResearchState) -> dict:
    return {
        "final_report": "This is not a research question."
    }


def route_after_evaluator(state: ResearchState) -> str:
    if state["evidence_sufficient"]:
        return "synthesizer"

    if state["research_iterations"] >= state["max_iterations"]:
        return "synthesizer"

    return "query_refiner"


def build_research_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("planner", planner_node)
    graph.add_node("searcher", search_node)
    graph.add_node("extractor", extractor_node)
    graph.add_node("ingestor", ingestion_node)
    graph.add_node("retriever", retriever_node)
    graph.add_node("evaluator", evaluate_evidence)
    graph.add_node("synthesizer", synthesizer_node)
    graph.add_node("query_refiner", query_refiner_node)
    graph.add_node("question_validator", validate_question)
    graph.add_node("non_research_response", non_research_response)
    

    graph.add_edge(START, "question_validator")
    graph.add_conditional_edges(
        "question_validator",
        route_after_validator,
        {
            "planner": "planner",
            "end": "non_research_response",
        },
    )
    graph.add_edge("non_research_response", END)
    graph.add_edge("planner", "searcher")
    graph.add_edge("searcher", "extractor")
    graph.add_edge("extractor", "ingestor")
    graph.add_edge("ingestor", "retriever")
    graph.add_edge("retriever", "evaluator")
    graph.add_conditional_edges(
        "evaluator",
        route_after_evaluator,
        {
            "synthesizer": "synthesizer",
            "query_refiner": "query_refiner",
        },
    )

    graph.add_edge("query_refiner", "searcher")
    graph.add_edge("synthesizer", END)

    return graph.compile()