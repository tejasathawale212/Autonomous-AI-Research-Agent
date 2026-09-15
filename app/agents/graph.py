from langgraph.graph import END, START, StateGraph

from app.agents.planner import planner_node
from app.agents.searcher import search_node
from app.agents.state import ResearchState
from app.agents.searcher import search_node

def build_research_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("planner", planner_node)
    graph.add_node("searcher", search_node)

    graph.add_edge(START, "planner")
    graph.add_edge("planner", "searcher")
    graph.add_edge("searcher", END)

    return graph.compile()