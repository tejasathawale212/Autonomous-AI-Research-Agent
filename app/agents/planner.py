import json

from app.services.llm import client
from pydantic import BaseModel
from app.agents.state import ResearchState
from app.prompts.planner import (
    PLANNER_SYSTEM_PROMPT,
    PLANNER_USER_PROMPT,
)


class ResearchPlan(BaseModel):
    objective: str
    sub_questions: list[str]
    search_queries: list[str]


def create_research_plan(question: str) -> ResearchPlan:
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": PLANNER_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": PLANNER_USER_PROMPT.format(
                    question=question
                ),
            },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "research_plan",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "objective": {"type": "string"},
                        "sub_questions": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "search_queries": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [
                        "objective",
                        "sub_questions",
                        "search_queries",
                    ],
                    "additionalProperties": False,
                },
            },
        },
    )

    data = json.loads(response.choices[0].message.content)

    return ResearchPlan.model_validate(data)




def planner_node(state: ResearchState) -> dict:
    plan = create_research_plan(state["question"])

    return{
            "objective": plan.objective,
            "sub_questions": plan.sub_questions,
            "search_queries": plan.search_queries,
        }