from app.agents.planner import create_research_plan


plan = create_research_plan(
    "What are the major challenges of deploying AI agents in production?"
)

print("\nObjective:")
print(plan.objective)

print("\nSub-questions:")
for question in plan.sub_questions:
    print("-", question)

print("\nSearch queries:")
for query in plan.search_queries:
    print("-", query)