from app.agents.research_agent import research


def main():
    query = input("What would you like me to research? ")

    result = research(query)

    print("\nResearch Result:\n")
    print(result)


if __name__ == "__main__":
    main()