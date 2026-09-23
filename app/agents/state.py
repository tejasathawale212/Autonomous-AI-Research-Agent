from typing import TypedDict


class ResearchState(TypedDict):
    research_id: str
    question: str
    objective: str
    sub_questions: list[str]
    search_queries: list[str]
    sources: list[dict]
    documents: list[dict]
    chunks: list[dict]
    retrieved_context: list[dict]
    findings: list[dict]
    final_report: str
    evidence_sufficient: bool
    research_iterations: int
    max_iterations: int
    is_research_question: bool



    