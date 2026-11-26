from typing_extensions import TypedDict
from langgraph.graph import MessagesState

class State(MessagesState):
    led: bool
    sense: bool
