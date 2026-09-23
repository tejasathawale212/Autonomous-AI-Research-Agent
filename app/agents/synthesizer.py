from app.agents.state import ResearchState
from app.services.llm import client
from app.prompts.synthesizer import (
    SYNTHESIZER_SYSTEM_PROMPT,
    SYNTHESIZER_USER_PROMPT,
)


def synthesizer_node(state: ResearchState) -> dict:
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
                "content": SYNTHESIZER_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": SYNTHESIZER_USER_PROMPT.format(
                    question=state["question"], 
                    context=context),
            },
        ],
    )

    return {
        "final_report": response.choices[0].message.content,
    }