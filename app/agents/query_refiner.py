from app.agents.state import ResearchState
from app.services.llm import client
from app.prompts.query_refiner import (
    QUERY_REFINER_SYSTEM_PROMPT,
    QUERY_REFINER_USER_PROMPT,
)


def query_refiner_node(state: ResearchState) -> dict:
    context = "\n\n".join(
        f"Source: {item['title']}\n"
        f"Content: {item['content']}"
        for item in state["retrieved_context"]
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": QUERY_REFINER_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": QUERY_REFINER_USER_PROMPT.format(
                    question=state["question"], 
                    context=context
                ),
            },
        ],
            
    )

    queries = [
        line.strip("- ").strip()
        for line in response.choices[0].message.content.splitlines()
        if line.strip()
    ]

    return {
        "search_queries": queries[:3],
        "research_iterations": state["research_iterations"] + 1,
    }