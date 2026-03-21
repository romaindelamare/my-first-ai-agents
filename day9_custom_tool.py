from crewai import Agent, Task, Crew
from crewai.tools import tool
from config import crew_llm

# 1. CUSTOM TOOL
@tool("calculate_battle_score")
def calculate_battle_score(hp: int, attack: int, defense: int) -> str:
    """
    Useful to calculate a Pokemon's secret battle score. 
    Formula: (Attack * 1.5) + Defense + (HP / 2).
    """
    score = (attack * 1.5) + defense + (hp / 2)
    return f"The calculated Battle Score is {score}"

# 2. THE AGENT
analyst = Agent(
    role='Pokemon Battle Analyst',
    goal='Calculate the secret battle score for {pokemon} using its base stats.',
    backstory='You are a data-driven coach who uses math to win battles.',
    tools=[calculate_battle_score],
    llm=crew_llm,
    verbose=True
)

# 4. THE TASK
task = Task(
    description='Find the base HP, Attack, and Defense for {pokemon}, then use the tool to find the score.',
    expected_output='A report containing the base stats and the final Battle Score.',
    agent=analyst
)

crew = Crew(agents=[analyst], tasks=[task])
result = crew.kickoff(inputs={'pokemon': 'Blastoise'})
print(result)

### LOG RESULT with Gemini ###
# Report:
# 
# Blastoise Base Stats:
# HP: 79
# Attack: 83
# Defense: 100
# 
# Blastoise Secret Battle Score: 264.0