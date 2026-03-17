from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from config import llm

class State(TypedDict):
    messages: Annotated[list, add_messages]

### 1. Define Tools ###
def get_pokemon_type(name: str):
    """Get the elemental type of a Pokemon by name."""
    print(f"TOOL: Executing tool get_pokemon_type for {name}")
    data = {"pikachu": "Electric", "charizard": "Fire/Flying"}
    return data.get(name.lower(), "Unknown")

tools = [get_pokemon_type]

# Bind tools so the LLM knows they exist
llm_with_tools = llm.bind_tools(tools)

### 2. Update the Node ###
def call_model(state: State):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

### 3. Rebuild the Graph ###
workflow = StateGraph(State)

workflow.add_node("chatbot", call_model)
# ToolNode is a built-in node that handles the execution for us
workflow.add_node("tools", ToolNode(tools))

workflow.add_edge(START, "chatbot")

# The "Conditional Edge" is the magic part. 
# tools_condition is a helper that checks if the LLM called a tool.
workflow.add_conditional_edges(
    "chatbot",
    tools_condition, 
)

# After the tools run, they MUST go back to the chatbot 
# so the LLM can see the result and give a final answer.
workflow.add_edge("tools", "chatbot")

app = workflow.compile()

if __name__ == "__main__":
    inputs = {"messages": [("user", "What is the type of Pikachu?")]}
    
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"Node '{key}' finished.")
            print(f"Response: {value['messages'][-1].content}")

### LOG RESULT with Gemini ###
# Node 'chatbot' finished.
# Response: 
# TOOL: Executing tool get_pokemon_type for Pikachu
# Node 'tools' finished.
# Response: Electric
# Node 'chatbot' finished.
# Response: Pikachu is an Electric type Pokemon.