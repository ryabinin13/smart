from config import get_llm
from prompts import CLASSIFIER_PROMPT, SHORT_ANSWER_PROMPT, LONG_ANSWER_PROMPT, SEARCH_DECISION_PROMPT
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from state import State

from langgraph.prebuilt import ToolNode, tools_condition

from tools import tools

llm = get_llm()

def agent_node(state):
    print("agent_node")

    # LLM ожидает список сообщений
    messages = state["messages"]
    
    answer = llm.invoke(messages)  # AIMessage

    print(state["messages"])

    # возвращаем только новое сообщение — редьюсер add_messages
    # сам добавит его к истории
    return {"messages": [answer]}


def route_web_search(state):
    if state['is_web'] == "search":
        return "web_node"
    return "classification_node"


def route_type_answer(state):
    if state["type_answer"] == "short":
        return "llm_node_short"
    return "llm_node_long"


builder = StateGraph(State)


builder.add_node("agent_node", agent_node)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "agent_node")
builder.add_conditional_edges("agent_node", tools_condition)
builder.add_edge("tools", "agent_node")

from langgraph.checkpoint.memory import MemorySaver

graph = builder.compile(checkpointer=MemorySaver())


if __name__ == "__main__":

    png_bytes = graph.get_graph().draw_mermaid_png()
    with open("graph.png", "wb") as f:
        f.write(png_bytes)
    print("Saved to graph.png")