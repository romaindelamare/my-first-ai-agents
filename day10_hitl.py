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

### Starting Human-in-the-Loop Workflow
# ╭─────────────────────────────────── 🚀 Crew Execution Started ───────────────────────────────────╮
# │                                                                                                 │
# │  Crew Execution Started                                                                         │
# │  Name: crew                                                                                     │
# │  ID: 7bf43ef9-ede0-4483-b7f0-31bc30775465                                                       │
# │                                                                                                 │
# │                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭──────────────────────────────────────── 📋 Task Started ────────────────────────────────────────╮
# │                                                                                                 │
# │  Task Started                                                                                   │
# │  Name:                                                                                          │
# │          1. Research the primary type and base stats of Gengar.                                 │
# │          2. Calculate its battle score using calculate_battle_score tool.                       │
# │          3. Draft a summary report.                                                             │
# │          4. SHOW the draft to the Human and ask for their feedback or approval.                 │
# │                                                                                                 │
# │  ID: b7cf4100-dde8-42b6-89d2-b80478c6669d                                                       │
# │                                                                                                 │
# │                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────╮
# │                                                                                                 │
# │  Agent: Lead Pokemon Researcher                                                                 │
# │                                                                                                 │
# │  Task:                                                                                          │
# │          1. Research the primary type and base stats of Gengar.                                 │
# │          2. Calculate its battle score using calculate_battle_score tool.                       │
# │          3. Draft a summary report.                                                             │
# │          4. SHOW the draft to the Human and ask for their feedback or approval.                 │
# │                                                                                                 │
# │                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────── ✅ Tool Execution Completed (#1) ────────────────────────────────╮
# │                                                                                                 │
# │  Tool Completed                                                                                 │
# │  Tool: calculate_battle_score                                                                   │
# │  Output: The calculated Battle Score is 187.5                                                   │
# │                                                                                                 │
# │                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
# Tool calculate_battle_score executed with result: The calculated Battle Score is 187.5...
# 
# ╭──────────────────────────────── 🔧 Tool Execution Started (#1) ─────────────────────────────────╮
# │                                                                                                 │
# │  Tool: calculate_battle_score                                                                   │
# │  Args: {'hp': 60, 'defense': 60, 'attack': 65}                                                  │
# │                                                                                                 │
# │                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────────╮
# │                                                                                                 │
# │  Agent: Lead Pokemon Researcher                                                                 │
# │                                                                                                 │
# │  Final Answer:                                                                                  │
# │  **Pokemon Battle Readiness Report: Gengar**                                                    │
# │                                                                                                 │
# │  **Type:** Ghost/Poison                                                                         │
# │                                                                                                 │
# │  **Base Stats:**                                                                                │
# │  *   HP: 60                                                                                     │
# │  *   Attack: 65                                                                                 │
# │  *   Defense: 60                                                                                │
# │                                                                                                 │
# │  **Calculated Battle Score:** 187.5                                                             │
# │                                                                                                 │
# │  **Analysis:**                                                                                  │
# │  Gengar, a Ghost/Poison-type Pokémon, possesses a unique typing that offers both strategic      │
# │  advantages and potential vulnerabilities in battle. Its base stats indicate a Pokémon that     │
# │  can deliver decent damage (Attack: 65) and withstand some hits (Defense: 60, HP: 60),          │
# │  contributing to a respectable battle score of 187.5. This score suggests Gengar is a capable   │
# │  combatant, particularly effective when utilizing its offensive capabilities. Its Ghost typing  │
# │  allows it to be immune to Normal and Fighting-type moves, while its Poison typing makes it     │
# │  resistant to Grass, Fighting, Poison, Bug, and Fairy moves. However, Gengar is vulnerable to   │
# │  Ground, Psychic, Ghost, and Dark-type attacks, which trainers must consider when deploying it  │
# │  in battle.                                                                                     │
# │                                                                                                 │
# │  **Conclusion:**                                                                                │
# │  Gengar demonstrates solid battle readiness with its balanced offensive and defensive stats,    │
# │  highlighted by its battle score. Its dual typing provides a mix of resistances and             │
# │  immunities, making it a versatile Pokémon for various matchups, provided its weaknesses are    │
# │  managed strategically.                                                                         │
# │                                                                                                 │
# │  Manager, this is a draft of Gengar's Battle Readiness Report. Please let me know if you have   │
# │  any feedback or if it meets your approval.                                                     │
# │                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────── 💬 Human Feedback Required ───────────────────────────────────╮
# │                                                                                                 │
# │  Provide feedback on the Final Result above.                                                    │
# │                                                                                                 │
# │  • If you are happy with the result, simply hit Enter without typing anything.                  │
# │  • Otherwise, provide specific improvement requests.                                            │
# │  • You can provide multiple rounds of feedback until satisfied.                                 │
# │                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
# The formatting is too messy. Please rewrite the report using bullet points and bold the final score.
# 
# Processing your feedback...
# ╭───────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────────╮
# │                                                                                                 │
# │  Agent: Lead Pokemon Researcher                                                                 │
# │                                                                                                 │
# │  Final Answer:                                                                                  │
# │  **Pokemon Battle Readiness Report: Gengar**                                                    │
# │                                                                                                 │
# │  *   **Type:** Ghost/Poison                                                                     │
# │  *   **Base Stats:**                                                                            │
# │      *   HP: 60                                                                                 │
# │      *   Attack: 65                                                                             │
# │      *   Defense: 60                                                                            │
# │  *   **Calculated Battle Score:** **187.5**                                                     │
# │                                                                                                 │
# │  **Analysis:**                                                                                  │
# │  Gengar, a Ghost/Poison-type Pokémon, possesses a unique typing that offers both strategic      │
# │  advantages and potential vulnerabilities in battle. Its base stats indicate a Pokémon that     │
# │  can deliver decent damage (Attack: 65) and withstand some hits (Defense: 60, HP: 60),          │
# │  contributing to a respectable battle score of 187.5. This score suggests Gengar is a capable   │
# │  combatant, particularly effective when utilizing its offensive capabilities. Its Ghost typing  │
# │  allows it to be immune to Normal and Fighting-type moves, while its Poison typing makes it     │
# │  resistant to Grass, Fighting, Poison, Bug, and Fairy moves. However, Gengar is vulnerable to   │
# │  Ground, Psychic, Ghost, and Dark-type attacks, which trainers must consider when deploying it  │
# │  in battle.                                                                                     │
# │                                                                                                 │
# │  **Conclusion:**                                                                                │
# │  Gengar demonstrates solid battle readiness with its balanced offensive and defensive stats,    │
# │  highlighted by its battle score. Its dual typing provides a mix of resistances and             │
# │  immunities, making it a versatile Pokémon for various matchups, provided its weaknesses are    │
# │  managed strategically.                                                                         │
# │                                                                                                 │
# │  Manager, this is a revised draft of Gengar's Battle Readiness Report, incorporating your       │
# │  feedback on formatting. Please let me know if you have any further feedback or if it meets     │
# │  your approval.                                                                                 │
# │                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────── 💬 Human Feedback Required ───────────────────────────────────╮
# │                                                                                                 │
# │  Provide feedback on the Final Result above.                                                    │
# │                                                                                                 │
# │  • If you are happy with the result, simply hit Enter without typing anything.                  │
# │  • Otherwise, provide specific improvement requests.                                            │
# │  • You can provide multiple rounds of feedback until satisfied.                                 │
# │                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────── 📋 Task Completion ───────────────────────────────────────╮
# │                                                                                                 │
# │  Task Completed                                                                                 │
# │  Name:                                                                                          │
# │          1. Research the primary type and base stats of Gengar.                                 │
# │          2. Calculate its battle score using calculate_battle_score tool.                       │
# │          3. Draft a summary report.                                                             │
# │          4. SHOW the draft to the Human and ask for their feedback or approval.                 │
# │                                                                                                 │
# │  Agent: Lead Pokemon Researcher                                                                 │
# │                                                                                                 │
# │                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭──────────────────────────────────────── Crew Completion ────────────────────────────────────────╮
# │                                                                                                 │
# │  Crew Execution Completed                                                                       │
# │  Name: crew                                                                                     │
# │  ID: 7bf43ef9-ede0-4483-b7f0-31bc30775465                                                       │
# │  Final Output: **Pokemon Battle Readiness Report: Gengar**                                      │
# │                                                                                                 │
# │  *   **Type:** Ghost/Poison                                                                     │
# │  *   **Base Stats:**                                                                            │
# │      *   HP: 60                                                                                 │
# │      *   Attack: 65                                                                             │
# │      *   Defense: 60                                                                            │
# │  *   **Calculated Battle Score:** **187.5**                                                     │
# │                                                                                                 │
# │  **Analysis:**                                                                                  │
# │  Gengar, a Ghost/Poison-type Pokémon, possesses a unique typing that offers both strategic      │
# │  advantages and potential vulnerabilities in battle. Its base stats indicate a Pokémon that     │
# │  can deliver decent damage (Attack: 65) and withstand some hits (Defense: 60, HP: 60),          │
# │  contributing to a respectable battle score of 187.5. This score suggests Gengar is a capable   │
# │  combatant, particularly effective when utilizing its offensive capabilities. Its Ghost typing  │
# │  allows it to be immune to Normal and Fighting-type moves, while its Poison typing makes it     │
# │  resistant to Grass, Fighting, Poison, Bug, and Fairy moves. However, Gengar is vulnerable to   │
# │  Ground, Psychic, Ghost, and Dark-type attacks, which trainers must consider when deploying it  │
# │  in battle.                                                                                     │
# │                                                                                                 │
# │  **Conclusion:**                                                                                │
# │  Gengar demonstrates solid battle readiness with its balanced offensive and defensive stats,    │
# │  highlighted by its battle score. Its dual typing provides a mix of resistances and             │
# │  immunities, making it a versatile Pokémon for various matchups, provided its weaknesses are    │
# │  managed strategically.                                                                         │
# │                                                                                                 │
# │  Manager, this is a revised draft of Gengar's Battle Readiness Report, incorporating your       │
# │  feedback on formatting. Please let me know if you have any further feedback or if it meets     │
# │  your approval.                                                                                 │
# │                                                                                                 │
# │                                                                                                 │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ########################
# ## FINAL APPROVED OUTPUT:
# ########################
# **Pokemon Battle Readiness Report: Gengar**
# 
# *   **Type:** Ghost/Poison
# *   **Base Stats:**
#     *   HP: 60
#     *   Attack: 65
#     *   Defense: 60
# *   **Calculated Battle Score:** **187.5**
# 
# **Analysis:**
# Gengar, a Ghost/Poison-type Pokémon, possesses a unique typing that offers both strategic advantages and potential vulnerabilities in battle. Its base stats indicate a Pokémon that can deliver decent damage (Attack: 65) and withstand some hits (Defense: 60, HP: 60), contributing to a respectable battle score of 187.5. This score suggests Gengar is a capable combatant, particularly effective when utilizing its offensive capabilities. Its Ghost typing allows it to be immune to Normal and Fighting-type moves, while its Poison typing makes it resistant to Grass, Fighting, Poison, Bug, and Fairy moves. However, Gengar is vulnerable to Ground, Psychic, Ghost, and Dark-type attacks, which trainers must consider when deploying it in battle.
# 
# **Conclusion:**
# Gengar demonstrates solid battle readiness with its balanced offensive and defensive stats, highlighted by its battle score. Its dual typing provides a mix of resistances and immunities, making it a versatile Pokémon for various matchups, provided its weaknesses are managed strategically.        
# 
# Manager, this is a revised draft of Gengar's Battle Readiness Report, incorporating your feedback on formatting. Please let me know if you have any further feedback or if it meets your approval.