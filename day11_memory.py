from crewai import Agent, Task, Crew
from config import crew_llm, crew_embedder, storage_path

historian = Agent(
    role='Grand Pokemon Archivist',
    goal='Research and store the legendary origins of {pokemon}.',
    backstory="""You maintain a permanent digital vault of all Pokemon lore.
    CRITICAL: When searching your memory, always provide search queries as a 
    simple list of strings. Do not wrap them in additional dictionaries or objects.""",
    llm=crew_llm,
    verbose=True
)

task = Task(
    description='Identify the ancient origins of {pokemon}.',
    expected_output='A detailed historical summary.',
    agent=historian
)

knowledge_crew = Crew(
    agents=[historian],
    tasks=[task],
    memory=True, # Enable the memory system
    embedder=crew_embedder,
    manager_llm=crew_llm,
    memory_config={
        "llm": crew_llm,
        "short_term_memory": {
            "enabled": True,
            "config": {"path": f"{storage_path}/short_term"}
        },
        "long_term_memory": {
            "enabled": True,
            "config": {"path": f"{storage_path}/long_term"}
        },
        "entity_memory": {
            "enabled": True,
            "config": {"path": f"{storage_path}/entity"}
        },
        "recall_memory": {
            "enabled": True,
            "config": {"path": f"{storage_path}/recall"}
        }
    },
    verbose=True
)

# Run the learning phase
print("\n--- TURN 1: LEARNING ---")
knowledge_crew.kickoff(inputs={'pokemon': 'Rayquaza'})

# Run the memory check phase
print("\n--- TURN 2: TESTING PERSISTENT MEMORY ---")
result = knowledge_crew.kickoff(inputs={'pokemon': 'the same Pokemon we just talked about'})

print("\n--- FINAL RESULT FROM MEMORY ---")
print(result)

### LOG RESULT with Ollama on Turn 2 (Turn 1 was commented out) ###

# --- FINAL RESULT FROM MEMORY ---
# Thought: I now know the final answer
# 
# Rayquaza's ancient origins are part of the legendary history of the Pokémon world, specifically tied to the ancient myths of the Great Pokémon realms. According to traditional lore, Rayquaza is believed to be one of the primordial legendary Pokémon from the prehistoric era of the world.
# 
# **Mythic Origins:**
# 
# According to various Pokémon lore traditions, Rayquaza's origins trace back to the dawn era when ancient celestial beings known as the "Ancient Guardians" were created. In these mythological accounts, the legendary beings lived in the heavens and were tasked with the creation of life and the maintenance of cosmic balance. Rayquaza emerged as one of these ancient celestial entities that existed long before the first Pokémon were created.
# 
# **Creation Legend:**
# 
# In the lore of the ancient civilizations of Palde and the land beyond the Sea of Calm, stories describe how Rayquaza emerged from the primordial chaos after the first creatures had begun to manifest from the earth. These beings were formed when the raw elements of the universe were concentrated through ancient magical energy.
# 
# **Cultural Significance:**
# 
# Over time, the legend of Rayquaza became deeply embedded in the cultural consciousness of the Pokémon world. This mythos explains various phenomena such as:
# 
# - The ancient storms that sweep through the land every generation
# - The mysterious presence of celestial energy in the deep ocean
# - The legend of the "Sky God" who was the ancestor of the first Pokémon
# 
# **Historical Documentation:**
# 
# According to the ancient archives and the legendary history books of the world, Rayquaza was first recorded in the ancient records by the first civilizations. Its legend predates the current era of the Pokémon world by thousands of generations, making it one of the oldest and most significant creatures in the universe.
# 
# This legendary history of Rayquaza is a cornerstone of the ancient lore that has shaped the understanding of the Pokémon world's origins and the relationship between ancient celestial beings and the first creatures.