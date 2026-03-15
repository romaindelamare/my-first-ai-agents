import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

### 1. DEFINE TOOLS (The same Python functions) ###
def get_pokemon_type(name: str):
    print(f"TOOL: Calling get_pokemon_type for {name}")
    data = {"pikachu": "Electric", "charizard": "Fire/Flying", "bulbasaur": "Grass/Poison"}
    return data.get(name.lower(), "Unknown")

def get_name_length(text: str):
    print(f"TOOL: Calling get_name_length for {text}")
    return len(text)

def add_numbers(a: int, b: int):
    print(f"TOOL: Calling add_numbers for {a} + {b}")
    return a + b

### 2. THE TOOL DEFINITION (The Schema) ###
# This tells Gemini exactly what the functions expect
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_pokemon_type",
            "description": "Get the elemental type of a Pokemon by name",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "The name of the Pokemon, e.g. Pikachu"}
                },
                "required": ["name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_name_length",
            "description": "Get the number of characters in a string",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "add_numbers",
            "description": "Add two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number to add"},
                    "b": {"type": "number", "description": "Second number to add"}
                },
                "required": ["a","b"],
            },
        },
    }
]

def run_agent_v2(question):
    print(f"QUESTION: {question}")

    messages = [
        {"role": "user", "content": question},
        {"role": "system", "content": "Identify all required data points and call the necessary tools in parallel where possible."}
    ]

    for _ in range(5):
        # Send the question + tool definitions
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        response_message = response.choices[0].message
        messages.append(response_message)

        tool_calls = response_message.tool_calls

        # If Gemini don't want to call tool, print final answer
        if not tool_calls:
            print(f"\nFINAL ANSWER: {response_message.content}")
            break

        # Call tools
        print(f"Gemini wants to call {len(tool_calls)} tool(s).")
        messages.append(response_message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            # Execute the actual function
            if function_name == "get_pokemon_type":
                result = get_pokemon_type(function_args.get("name"))
            elif function_name == "get_name_length":
                result = get_name_length(function_args.get("text"))
            elif function_name == "add_numbers":
                result = add_numbers(function_args.get("a"), function_args.get("b"))
            
            print(f"Executing {function_name} with {function_args} -> Result: {result}")

            # Send the result back to Gemini
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": str(result),
            })

#run_agent_v2("What is the type of Bulbasaur and how many letters are in its name?")

# QUESTION: What is the type of Bulbasaur and how many letters are in its name?
# Gemini wants to call 2 tool(s).
# TOOL: Calling get_pokemon_type for Bulbasaur
# Executing get_pokemon_type with {'name': 'Bulbasaur'} -> Result: Grass/Poison
# TOOL: Calling get_name_length for Bulbasaur
# Executing get_name_length with {'text': 'Bulbasaur'} -> Result: 9
# 
# FINAL ANSWER: Bulbasaur is a **Grass/Poison** type Pokémon, and there are **9** letters in its name.

#run_agent_v2("Compare the lengths of the names 'Bulbasaur', 'Charmander', and 'Squirtle'.")

# QUESTION: Compare the lengths of the names 'Bulbasaur', 'Charmander', and 'Squirtle'.
# Gemini wants to call 3 tool(s).
# TOOL: Calling get_name_length for Bulbasaur
# Executing get_name_length with {'text': 'Bulbasaur'} -> Result: 9
# TOOL: Calling get_name_length for Charmander
# Executing get_name_length with {'text': 'Charmander'} -> Result: 10
# TOOL: Calling get_name_length for Squirtle
# Executing get_name_length with {'text': 'Squirtle'} -> Result: 8
# 
# FINAL ANSWER: Here's a comparison of the lengths of the names:
# 
# *   **Bulbasaur:** 9 characters
# *   **Charmander:** 10 characters
# *   **Squirtle:** 8 characters
# 
# Comparing them:
# *   **Charmander** is the longest name with 10 characters.
# *   **Squirtle** is the shortest name with 8 characters.
# *   **Bulbasaur** is in the middle with 9 characters.

run_agent_v2("What is the sum of the number of letters in Pikachu and Bulbasaur?")

# QUESTION: What is the sum of the number of letters in Pikachu and Bulbasaur?
# Gemini wants to call 2 tool(s).
# TOOL: Calling get_name_length for Pikachu
# Executing get_name_length with {'text': 'Pikachu'} -> Result: 7
# TOOL: Calling get_name_length for Bulbasaur
# Executing get_name_length with {'text': 'Bulbasaur'} -> Result: 9
# Gemini wants to call 1 tool(s).
# TOOL: Calling add_numbers for 7 + 9
# Executing add_numbers with {'a': 7, 'b': 9} -> Result: 16
# 
# FINAL ANSWER: The sum of the number of letters in Pikachu and Bulbasaur is 16.