from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from config import llm

class State(TypedDict):
    messages: Annotated[list, add_messages]

def get_pokemon_type(name: str):
    """Get the elemental type of a Pokemon by name."""
    print(f"TOOL: Executing tool get_pokemon_type for {name}")
    data = {"pikachu": "Electric", "charizard": "Fire/Flying"}
    return data.get(name.lower(), "Unknown")

def get_name_length(text: str):
    """Get the number of characters in a string."""
    print(f"TOOL: Calling get_name_length for {text}")
    return len(text)

tools = [get_pokemon_type, get_name_length]

llm_with_tools = llm.bind_tools(tools)

def call_model(state: State):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

workflow = StateGraph(State)
workflow.add_node("chatbot", call_model)
workflow.add_node("tools", ToolNode(tools))
workflow.add_edge(START, "chatbot")
workflow.add_conditional_edges(
    "chatbot",
    tools_condition, 
)
workflow.add_edge("tools", "chatbot")

# Initialize Memory
memory = MemorySaver()

# Compile the graph with the checkpointer
app = workflow.compile(checkpointer=memory)

# Running with a "Thread ID"
# To remember a conversation, you must provide a unique ID
config = {"configurable": {"thread_id": "id_chat_1"}}

# --- TEST TURN 1 ---
input_1 = {"messages": [("user", "What is Pikachu's type?")]}
for event in app.stream(input_1, config):
    pass # Let it process

# --- TEST TURN 2 ---
input_2 = {"messages": [("user", "And how many letters are in its name?")]}
for event in app.stream(input_2, config):
    for value in event.values():
        print(value["messages"][-1].content)

### LOG RESULT with Gemini ###
# TOOL: Executing tool get_pokemon_type for Pikachu
# 
# TOOL: Calling get_name_length for Pikachu
# 7
# Pikachu has 7 letters in its name.