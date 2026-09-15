from typing import TypedDict


class ResearchState(TypedDict):
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