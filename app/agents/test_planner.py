from app.agents.planner import create_research_plan


question = "What are the major challenges of deploying AI agents in production?"

plan = create_research_plan(question)

print("\nOBJECTIVE:")
print(plan.objective)

print("\nSUB-QUESTIONS:")
for item in plan.sub_questions:
    print("-", item)

print("\nSEARCH QUERIES:")
for query in plan.search_queries:
    print("-", query)