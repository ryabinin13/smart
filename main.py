from graph import graph
from langchain_core.messages import HumanMessage

if __name__ == "__main__":
    config = {"configurable": {"thread_id": "user-1"}}

    while True:
        question = input("You: ")
        if question.strip() in {"exit", "quit"}:
            break

        result = graph.invoke(
            {"messages": [HumanMessage(content=question)], "led": True, "sense": True},
            config,
        )
        print("AI:", result["messages"][-1].content)