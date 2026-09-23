from app.agents.state import ResearchState
from app.services.llm import client
from app.prompts.evaluator import (
    EVALUATOR_SYSTEM_PROMPT,
    EVALUATOR_USER_PROMPT,
)


def evaluate_evidence(state: ResearchState) -> dict:
    context = "\n\n".join(
        f"Source: {item['title']}\n"
        f"URL: {item['url']}\n"
        f"Content: {item['content']}"
        for item in state["retrieved_context"]
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": EVALUATOR_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": EVALUATOR_USER_PROMPT.format(
                    question=state["question"], 
                    context=context
                ),
            },
        ],
    )

    decision = response.choices[0].message.content.strip().upper()

    return {
        "evidence_sufficient": decision == "YES"
    }