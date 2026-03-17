from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from config import llm

class State(TypedDict):
    # 'add_messages' ensures that when a node returns a message, 
    # it appends to the history instead of overwriting it.
    messages: Annotated[list, add_messages]

def call_model(state: State):
    response = llm.invoke(state["messages"])
    # We return a dictionary that matches our State key
    return {"messages": [response]}

# 1. Initialize the graph with our State definition
workflow = StateGraph(State)

# 2. Add the node we created
workflow.add_node("chatbot", call_model)

# 3. Define the edges (The "Roadmap")
workflow.add_edge(START, "chatbot")
workflow.add_edge("chatbot", END)

# 4. Compile the graph into an executable app
app = workflow.compile()

if __name__ == "__main__":
    inputs = {"messages": [("user", "Hi, my name is Romain. What's yours?")]}
    
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"Node '{key}' finished.")
            print(f"Response: {value['messages'][-1].content}")

### LOG RESULT with Gemini ###
# Node 'chatbot' finished.
# Response: Hi Romain! I don't have a name. I'm a large language model, trained by Google.
# 
# It's nice to meet you! How can I help you today?