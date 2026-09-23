from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.agents.research_agent import research


app = FastAPI(title="Autonomous AI Research Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResearchRequest(BaseModel):
    question: str


class ResearchSource(BaseModel):
    title: str
    url: str
    query: str


class ResearchResponse(BaseModel):
    result: str
    sources: list[ResearchSource]


@app.get("/")
def root():
    return {"message": "Autonomous AI Research Agent API is running"}


@app.post("/research", response_model=ResearchResponse)
def run_research(request: ResearchRequest):
    result = research(request.question)

    return ResearchResponse(
        result=result["final_report"],
        sources=result["sources"],
    )

