from crewai import Agent, Task, Crew
from crewai_tools import DirectoryReadTool
import config

directory_reader = DirectoryReadTool(directory='./knowledge')

# Add to the manager the ability to delegate tasks to other agents.
manager = Agent(
    role='Project Manager',
    goal='Ensure the Pokemon mineral report is accurate and complete.',
    backstory='You coordinate specialists to get the best data possible.',
    llm=config.crew_llm,
    allow_delegation=True,
    verbose=True
)

researcher = Agent(
    role='Mineral Researcher',
    goal='Locate mineral names in local files.',
    backstory='You are a specialist in reading documentation.',
    llm=config.crew_llm,
    tools=[directory_reader],
    verbose=True
)

coordinated_task = Task(
    description="""
        Coordinate the research of 'rayquaza_lore.txt' and 'kyogre_lore.txt'.
        Ensure we have the mineral name for both.
    """,
    expected_output='A final confirmed report of both minerals.',
    agent=manager # Assigned to Manager
)

collaboration_crew = Crew(
    agents=[manager, researcher],
    tasks=[coordinated_task],
    process='sequential', # Manager leads the sequence
    verbose=True
)

print("\n--- STARTING DELEGATION FLOW ---")
result = collaboration_crew.kickoff()
print(result)

### LOG RESULT with Gemini ###
# ╭────────────────────────────────────────────── ✨ Update Available ✨ ───────────────────────────────────────────────╮
# │                                                                                                                     │
# │  A new version of CrewAI is available!                                                                              │
# │                                                                                                                     │
# │  Current version: 1.11.0                                                                                            │
# │  Latest version:  1.11.1                                                                                            │
# │                                                                                                                     │
# │  To update, run: uv sync --upgrade-package crewai                                                                   │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────── 🚀 Crew Execution Started ─────────────────────────────────────────────╮
# │                                                                                                                     │
# │  Crew Execution Started                                                                                             │
# │  Name: crew                                                                                                         │
# │  ID: 3c7ba994-bcdb-4fba-8128-81cc9a176f16                                                                           │
# │                                                                                                                     │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────────── 📋 Task Started ──────────────────────────────────────────────────╮
# │                                                                                                                     │
# │  Task Started                                                                                                       │
# │  Name:                                                                                                              │
# │          Coordinate the research of 'rayquaza_lore.txt' and 'kyogre_lore.txt'.                                      │
# │          Ensure we have the mineral name for both.                                                                  │
# │                                                                                                                     │
# │  ID: 4a678ec6-1749-4df2-b157-73d618713015                                                                           │
# │                                                                                                                     │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────────── 🤖 Agent Started ──────────────────────────────────────────────────╮
# │                                                                                                                     │
# │  Agent: Project Manager                                                                                             │
# │                                                                                                                     │
# │  Task:                                                                                                              │
# │          Coordinate the research of 'rayquaza_lore.txt' and 'kyogre_lore.txt'.                                      │
# │          Ensure we have the mineral name for both.                                                                  │
# │                                                                                                                     │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────── 🔧 Tool Execution Started (#1) ───────────────────────────────────────────╮
# │                                                                                                                     │
# │  Tool: delegate_work_to_coworker                                                                                    │
# │  Args: {'coworker': 'Mineral Researcher', 'task': "Identify the mineral name associated with Rayquaza from the      │
# │  provided lore. The lore explicitly mentions a mineral that is tied to Rayquaza's power.", 'conte...                │
# │                                                                                                                     │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────── 🔧 Tool Execution Started (#2) ───────────────────────────────────────────╮
# │                                                                                                                     │
# │  Tool: delegate_work_to_coworker                                                                                    │
# │  Args: {'coworker': 'Mineral Researcher', 'task': "Identify the mineral name associated with Kyogre from the        │
# │  provided lore. The lore explicitly mentions a mineral that is tied to Kyogre's power.", 'context':...              │
# │                                                                                                                     │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────────── 🤖 Agent Started ──────────────────────────────────────────────────╮
# │                                                                                                                     │
# │  Agent: Mineral Researcher                                                                                          │
# │                                                                                                                     │
# │  Task: Identify the mineral name associated with Kyogre from the provided lore. The lore explicitly mentions a      │
# │  mineral that is tied to Kyogre's power.                                                                            │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────────── 🤖 Agent Started ──────────────────────────────────────────────────╮
# │                                                                                                                     │
# │  Agent: Mineral Researcher                                                                                          │
# │                                                                                                                     │
# │  Task: Identify the mineral name associated with Kyogre from the provided lore. The lore explicitly mentions a      │
# │  mineral that is tied to Kyogre's power.                                                                            │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────────── ✅ Agent Final Answer ───────────────────────────────────────────────╮
# │                                                                                                                     │
# │  Agent: Mineral Researcher                                                                                          │
# │                                                                                                                     │
# │  Final Answer:                                                                                                      │
# │  Kyogre's power is tied to "marine crystal".                                                                        │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────── ✅ Tool Execution Completed (#2) ──────────────────────────────────────────╮
# │                                                                                                                     │
# │  Tool Completed                                                                                                     │
# │  Tool: delegate_work_to_coworker                                                                                    │
# │  Output: Kyogre's power is tied to "marine crystal".                                                                │
# │                                                                                                                     │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────────── ✅ Agent Final Answer ───────────────────────────────────────────────╮
# │                                                                                                                     │
# │  Agent: Mineral Researcher                                                                                          │
# │                                                                                                                     │
# │  Final Answer:                                                                                                      │
# │  The mineral name associated with Rayquaza is Jade.                                                                 │
# │  The mineral name associated with Kyogre is marine crystal.                                                         │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────── ✅ Tool Execution Completed (#2) ──────────────────────────────────────────╮
# │                                                                                                                     │
# │  Tool Completed                                                                                                     │
# │  Tool: delegate_work_to_coworker                                                                                    │
# │  Output: The mineral name associated with Rayquaza is Jade.                                                         │
# │  The mineral name associated with Kyogre is marine crystal.                                                         │
# │                                                                                                                     │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# Tool delegate_work_to_coworker executed with result: The mineral name associated with Rayquaza is Jade.
# The mineral name associated with Kyogre is marine crystal....
# Tool delegate_work_to_coworker executed with result: Kyogre's power is tied to "marine crystal"....
# ╭─────────────────────────────────────────────── ✅ Agent Final Answer ───────────────────────────────────────────────╮
# │                                                                                                                     │
# │  Agent: Project Manager                                                                                             │
# │                                                                                                                     │
# │  Final Answer:                                                                                                      │
# │  Rayquaza: Jade                                                                                                     │
# │  Kyogre: marine crystal                                                                                             │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭──────────────────────────────────────────────── 📋 Task Completion ─────────────────────────────────────────────────╮
# │                                                                                                                     │
# │  Task Completed                                                                                                     │
# │  Name:                                                                                                              │
# │          Coordinate the research of 'rayquaza_lore.txt' and 'kyogre_lore.txt'.                                      │
# │          Ensure we have the mineral name for both.                                                                  │
# │                                                                                                                     │
# │  Agent: Project Manager                                                                                             │
# │                                                                                                                     │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────────── Crew Completion ──────────────────────────────────────────────────╮
# │                                                                                                                     │
# │  Crew Execution Completed                                                                                           │
# │  Name: crew                                                                                                         │
# │  ID: 3c7ba994-bcdb-4fba-8128-81cc9a176f16                                                                           │
# │  Final Output: Rayquaza: Jade                                                                                       │
# │  Kyogre: marine crystal                                                                                             │
# │                                                                                                                     │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────────── Tracing Status ───────────────────────────────────────────────────╮
# │                                                                                                                     │
# │  Info: Tracing is disabled.                                                                                         │
# │                                                                                                                     │
# │  To enable tracing, do any one of these:                                                                            │
# │  • Set tracing=True in your Crew/Flow code                                                                          │
# │  • Set CREWAI_TRACING_ENABLED=true in your project's .env file                                                      │
# │  • Run: crewai traces enable                                                                                        │
# │                                                                                                                     │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# Rayquaza: Jade
# Kyogre: marine crystal