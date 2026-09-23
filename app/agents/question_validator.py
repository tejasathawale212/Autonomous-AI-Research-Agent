from app.agents.state import ResearchState
from app.services.llm import client


VALIDATOR_PROMPT = """
    You are a research-question classifier for an autonomous web research agent.

    Your task is to decide whether the user's request requires the agent to
    conduct research using external sources.

    CLASSIFY AS RESEARCH when answering properly would require one or more of:
    - Gathering information from multiple external sources.
    - Investigating a topic, problem, trend, event, or phenomenon.
    - Comparing products, technologies, companies, approaches, markets, or ideas
    using evidence.
    - Analyzing causes, effects, challenges, opportunities, risks, or trends.
    - Finding current, recent, historical, or source-based information.
    - Conducting academic, technical, business, market, industry, or similar research.
    - Finding evidence, statistics, studies, reports, or documented information.
    - Answering a broad question where reliable source-based investigation is needed.

    CLASSIFY AS NOT_RESEARCH when the request can be completed without conducting
    external research, such as:
    - Simple calculations or conversions.
    - Simple definitions or basic explanations.
    - Writing, rewriting, proofreading, translation, or summarization of supplied text.
    - Programming/code generation or debugging.
    - Casual conversation.
    - Personal advice or opinions.
    - Simple greetings or conversational requests.
    - A straightforward factual question that does not require source-based
    investigation.

    IMPORTANT:
    Judge the user's actual request, not whether it contains words such as
    "research", "study", "analyze", or "find".

    If the user explicitly asks to research, investigate, compare, verify, find
    evidence, or gather information from sources, classify it as RESEARCH when
    the request genuinely requires external investigation.

    Examples:

    "What are the main challenges of implementing AI agents in enterprises?"
    → RESEARCH

    "Compare LangGraph, CrewAI, and AutoGen for production AI agents."
    → RESEARCH

    "What are the latest trends in GenAI jobs in India?"
    → RESEARCH

    "Find studies about AI adoption in Indian companies."
    → RESEARCH

    "What is Python?"
    → NOT_RESEARCH

    "What is 25 multiplied by 4?"
    → NOT_RESEARCH

    "Write a Python program to calculate factorial."
    → NOT_RESEARCH

    "Rewrite this paragraph professionally."
    → NOT_RESEARCH

    "Explain what RAG means."
    → NOT_RESEARCH

    Return ONLY:
    RESEARCH
    or
    NOT_RESEARCH

    USER REQUEST:
    {question}
"""


def validate_question(state: ResearchState) -> dict:
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": VALIDATOR_PROMPT.format(
                    question=state["question"]
                ),
            }
        ],
    )

    decision = response.choices[0].message.content.strip().upper()

    return {
        "is_research_question": decision == "RESEARCH"
    }