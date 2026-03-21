from crewai import Agent, Task, Crew
from crewai.tools import tool
from config import crew_llm

@tool("calculate_battle_score")
def calculate_battle_score(hp: int, attack: int, defense: int) -> str:
    """
    Useful to calculate a Pokemon's secret battle score. 
    Formula: (Attack * 1.5) + Defense + (HP / 2).
    """
    score = (attack * 1.5) + defense + (hp / 2)
    return f"The calculated Battle Score is {score}"

researcher = Agent(
    role='Lead Pokemon Researcher',
    goal='Prepare a comprehensive battle readiness report for {pokemon}.',
    backstory="""You are an expert analyst. You don't just find stats; 
    you explain why they matter. However, you are humble and always 
    seek your manager's (the Human's) approval before finalizing a report.""",
    tools=[calculate_battle_score],
    llm=crew_llm,
    verbose=True,
    allow_delegation=False
)

# Define the Task with Human-in-the-Loop
approval_task = Task(
    description="""
        1. Research the primary type and base stats of {pokemon}.
        2. Calculate its battle score using calculate_battle_score tool.
        3. Draft a summary report.
        4. SHOW the draft to the Human and ask for their feedback or approval.
    """,
    expected_output='A final, human-approved Pokemon Battle Readiness Report.',
    agent=researcher,
    human_input=True
)

crew = Crew(
    agents=[researcher],
    tasks=[approval_task],
    verbose=True
)

print("### Starting Human-in-the-Loop Workflow")

result = crew.kickoff(inputs={'pokemon': 'Gengar'})

print("########################")
print("## FINAL APPROVED OUTPUT:")
print("########################")
print(result)


### LOG RESULT with Gemini ###

# ### Starting Human-in-the-Loop Workflow
# ╭─────────────────────────────────────────── 🚀 Crew Execution Started ───────────────────────────────────────────╮
# │                                                                                                                 │
# │  Crew Execution Started                                                                                         │
# │  Name: crew                                                                                                     │
# │  ID: 8a14ca3e-61c6-42de-bbff-44482707a84e                                                                       │
# │                                                                                                                 │
# │                                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭──────────────────────────────────────────────── 📋 Task Started ────────────────────────────────────────────────╮
# │                                                                                                                 │
# │  Task Started                                                                                                   │
# │  Name:                                                                                                          │
# │          1. Research the primary type and base stats of Gengar.                                                 │
# │          2. Calculate its battle score using calculate_battle_score tool.                                       │
# │          3. Draft a summary report.                                                                             │
# │          4. SHOW the draft to the Human and ask for their feedback or approval.                                 │
# │                                                                                                                 │
# │  ID: be6d28e7-0ce3-420e-88a7-4081b8dfdcc6                                                                       │
# │                                                                                                                 │
# │                                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────╮
# │                                                                                                                 │
# │  Agent: Lead Pokemon Researcher                                                                                 │
# │                                                                                                                 │
# │  Task:                                                                                                          │
# │          1. Research the primary type and base stats of Gengar.                                                 │
# │          2. Calculate its battle score using calculate_battle_score tool.                                       │
# │          3. Draft a summary report.                                                                             │
# │          4. SHOW the draft to the Human and ask for their feedback or approval.                                 │
# │                                                                                                                 │
# │                                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────── ✅ Tool Execution Completed (#1) ────────────────────────────────────────╮
# │                                                                                                                 │
# │  Tool Completed                                                                                                 │
# │  Tool: calculate_battle_score                                                                                   │
# │  Output: The calculated Battle Score is 187.5                                                                   │
# │                                                                                                                 │
# │                                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# Tool calculate_battle_score executed with result: The calculated Battle Score is 187.5...
# 
# ╭──────────────────────────────────────── 🔧 Tool Execution Started (#1) ─────────────────────────────────────────╮
# │                                                                                                                 │
# │  Tool: calculate_battle_score                                                                                   │
# │  Args: {'defense': 60, 'hp': 60, 'attack': 65}                                                                  │
# │                                                                                                                 │
# │                                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────────────────╮
# │                                                                                                                 │
# │  Agent: Lead Pokemon Researcher                                                                                 │
# │                                                                                                                 │
# │  Final Answer:                                                                                                  │
# │  Gengar Battle Readiness Report (Draft)                                                                         │
# │                                                                                                                 │
# │  **Pokemon:** Gengar                                                                                            │
# │  **Primary Type:** Ghost/Poison                                                                                 │
# │  **Base Stats:**                                                                                                │
# │  *   HP: 60                                                                                                     │
# │  *   Attack: 65                                                                                                 │
# │  *   Defense: 60                                                                                                │
# │  *   Special Attack: 130                                                                                        │
# │  *   Special Defense: 75                                                                                        │
# │  *   Speed: 110                                                                                                 │
# │                                                                                                                 │
# │  **Calculated Battle Score:** 187.5                                                                             │
# │                                                                                                                 │
# │  **Analysis:**                                                                                                  │
# │  Gengar, a Ghost/Poison-type Pokémon, possesses a Calculated Battle Score of 187.5. This score is derived from  │
# │  its physical attributes (Attack, Defense, and HP). While Gengar's raw physical stats (65 Attack, 60 Defense,   │
# │  60 HP) are not outstanding, its true power lies in its incredibly high Special Attack (130) and impressive     │
# │  Speed (110).                                                                                                   │
# │                                                                                                                 │
# │  The Battle Score of 187.5, focusing on physical bulk and attack, highlights an area where Gengar is not a      │
# │  premier tank or physical attacker. However, this merely underscores its role as a fast, special offensive      │
# │  threat. Its lower physical defense and HP mean it should avoid direct physical confrontations. Its high        │
# │  Special Attack and Speed allow it to strike first and hard with powerful special attacks, potentially          │
# │  knocking out opponents before they can retaliate effectively. Its Ghost/Poison typing also gives it unique     │
# │  resistances and immunities, which can be leveraged strategically.                                              │
# │                                                                                                                 │
# │  In summary, while its physical battle score is modest, Gengar's overall battle readiness is high due to its    │
# │  exceptional special attacking capabilities and speed, making it a formidable special sweeper or hit-and-run    │
# │  attacker.                                                                                                      │
# │                                                                                                                 │
# │  Manager, I have drafted this initial battle readiness report for Gengar. Could I get your feedback or          │
# │  approval before finalizing it?                                                                                 │
# │                                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────── 💬 Human Feedback Required ───────────────────────────────────────────╮
# │                                                                                                                 │
# │  Provide feedback on the Final Result above.                                                                    │
# │                                                                                                                 │
# │  • If you are happy with the result, simply hit Enter without typing anything.                                  │
# │  • Otherwise, provide specific improvement requests.                                                            │
# │  • You can provide multiple rounds of feedback until satisfied.                                                 │
# │                                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 📋 Task Completion ───────────────────────────────────────────────╮
# │                                                                                                                 │
# │  Task Completed                                                                                                 │
# │  Name:                                                                                                          │
# │          1. Research the primary type and base stats of Gengar.                                                 │
# │          2. Calculate its battle score using calculate_battle_score tool.                                       │
# │          3. Draft a summary report.                                                                             │
# │          4. SHOW the draft to the Human and ask for their feedback or approval.                                 │
# │                                                                                                                 │
# │  Agent: Lead Pokemon Researcher                                                                                 │
# │                                                                                                                 │
# │                                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭──────────────────────────────────────────────── Crew Completion ────────────────────────────────────────────────╮
# │                                                                                                                 │
# │  Crew Execution Completed                                                                                       │
# │  Name: crew                                                                                                     │
# │  ID: 8a14ca3e-61c6-42de-bbff-44482707a84e                                                                       │
# │  Final Output: Gengar Battle Readiness Report (Draft)                                                           │
# │                                                                                                                 │
# │  **Pokemon:** Gengar                                                                                            │
# │  **Primary Type:** Ghost/Poison                                                                                 │
# │  **Base Stats:**                                                                                                │
# │  *   HP: 60                                                                                                     │
# │  *   Attack: 65                                                                                                 │
# │  *   Defense: 60                                                                                                │
# │  *   Special Attack: 130                                                                                        │
# │  *   Special Defense: 75                                                                                        │
# │  *   Speed: 110                                                                                                 │
# │                                                                                                                 │
# │  **Calculated Battle Score:** 187.5                                                                             │
# │                                                                                                                 │
# │  **Analysis:**                                                                                                  │
# │  Gengar, a Ghost/Poison-type Pokémon, possesses a Calculated Battle Score of 187.5. This score is derived from  │
# │  its physical attributes (Attack, Defense, and HP). While Gengar's raw physical stats (65 Attack, 60 Defense,   │
# │  60 HP) are not outstanding, its true power lies in its incredibly high Special Attack (130) and impressive     │
# │  Speed (110).                                                                                                   │
# │                                                                                                                 │
# │  The Battle Score of 187.5, focusing on physical bulk and attack, highlights an area where Gengar is not a      │
# │  premier tank or physical attacker. However, this merely underscores its role as a fast, special offensive      │
# │  threat. Its lower physical defense and HP mean it should avoid direct physical confrontations. Its high        │
# │  Special Attack and Speed allow it to strike first and hard with powerful special attacks, potentially          │
# │  knocking out opponents before they can retaliate effectively. Its Ghost/Poison typing also gives it unique     │
# │  resistances and immunities, which can be leveraged strategically.                                              │
# │                                                                                                                 │
# │  In summary, while its physical battle score is modest, Gengar's overall battle readiness is high due to its    │
# │  exceptional special attacking capabilities and speed, making it a formidable special sweeper or hit-and-run    │
# │  attacker.                                                                                                      │
# │                                                                                                                 │
# │  Manager, I have drafted this initial battle readiness report for Gengar. Could I get your feedback or          │
# │  approval before finalizing it?                                                                                 │
# │                                                                                                                 │
# │                                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ########################
# ## FINAL APPROVED OUTPUT:
# ########################
# Gengar Battle Readiness Report (Draft)
# 
# **Pokemon:** Gengar
# **Primary Type:** Ghost/Poison
# **Base Stats:**
# *   HP: 60
# *   Attack: 65
# *   Defense: 60
# *   Special Attack: 130
# *   Special Defense: 75
# *   Speed: 110
# 
# **Calculated Battle Score:** 187.5
# 
# **Analysis:**
# Gengar, a Ghost/Poison-type Pokémon, possesses a Calculated Battle Score of 187.5. This score is derived from its physical attributes (Attack, Defense, and HP). While Gengar's raw physical stats (65 Attack, 60 Defense, 60 HP) are not outstanding, its true power lies in its incredibly high Special Attack (130) and impressive Speed (110).       
# 
# The Battle Score of 187.5, focusing on physical bulk and attack, highlights an area where Gengar is not a premier tank or physical attacker. However, this merely underscores its role as a fast, special offensive threat. Its lower physical defense and HP mean it should avoid direct physical confrontations. Its high Special Attack and Speed allow it to strike first and hard with powerful special attacks, potentially knocking out opponents before they can retaliate effectively. Its Ghost/Poison typing also gives it unique resistances and immunities, which can be leveraged strategically.
# 
# In summary, while its physical battle score is modest, Gengar's overall battle readiness is high due to its exceptional special attacking capabilities and speed, making it a formidable special sweeper or hit-and-run attacker.     
# 
# Manager, I have drafted this initial battle readiness report for Gengar. Could I get your feedback or approval before finalizing it?