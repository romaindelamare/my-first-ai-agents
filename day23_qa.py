from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool
import config

# 1. THE TOOL
lore_tool = FileReadTool(file_path='knowledge/rayquaza_lore.txt')

# 2. THE AGENTS
worker = Agent(
    role="Junior Researcher",
    goal="Find the mineral name in the lore file.",
    backstory="You are fast but sometimes forgetful. You MUST use the tool.",
    llm=config.crew_llm,
    tools=[lore_tool],
    verbose=True
)

critic = Agent(
    role="Senior Quality Auditor",
    goal="Verify that the Junior Researcher used the tool and found the right info.",
    backstory="""You are a perfectionist. If the researcher didn't use 
    the 'read_a_files_content' tool, or if the report is too short, 
    you must demand a rewrite. You are the final gatekeeper.""",
    llm=config.crew_llm,
    verbose=True
)

# 3. THE TASKS
research_task = Task(
    description="""
        1. Read knowledge/rayquaza_lore.txt.
        2. Identify the mineral name.
        3. YOU MUST INCLUDE THIS SECTION IN YOUR OUTPUT:
           'Proof of Tool Use: I accessed the file and found [mineral].'
    """,
    expected_output="A report with a 'Proof of Tool Use' section and the mineral name.",
    agent=worker
)

qa_task = Task(
    description="""
        Review the report in the context.
        If the 'Proof of Tool Use' section is missing, explain why you are rejecting it.
        If it's there and the mineral is 'Aether-Quartz', simply output 'FINAL VERIFIED REPORT: [Content]'.
    """,
    expected_output="The final verified report or a detailed rejection.",
    agent=critic,
    context=[research_task]
)

# 4. THE CREW
qa_crew = Crew(
    agents=[worker, critic],
    tasks=[research_task, qa_task],
    process='sequential',
    verbose=True
)

print("### DAY 23: SELF-CORRECTION & QA LOOP")
result = qa_crew.kickoff()

### LOG RESULT with Gemini ###

# ╭────────────────────────────────────────── 🚀 Crew Execution Started ───────────────────────────────────────────╮
# │                                                                                                                │
# │  Crew Execution Started                                                                                        │
# │  Name: crew                                                                                                    │
# │  ID: abb40399-2ade-4520-8343-b4c0e9f969cb                                                                      │
# │                                                                                                                │
# │                                                                                                                │
# ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────────── 📋 Task Started ────────────────────────────────────────────────╮
# │                                                                                                                │
# │  Task Started                                                                                                  │
# │  Name:                                                                                                         │
# │          1. Read knowledge/rayquaza_lore.txt.                                                                  │
# │          2. Identify the mineral name.                                                                         │
# │          3. YOU MUST INCLUDE THIS SECTION IN YOUR OUTPUT:                                                      │
# │             'Proof of Tool Use: I accessed the file and found [mineral].'                                      │
# │                                                                                                                │
# │  ID: e7fc7d1e-1d56-4ea1-84a9-68df83b9e459                                                                      │
# │                                                                                                                │
# │                                                                                                                │
# ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────────── 🤖 Agent Started ───────────────────────────────────────────────╮
# │                                                                                                                │
# │  Agent: Junior Researcher                                                                                      │
# │                                                                                                                │
# │  Task:                                                                                                         │
# │          1. Read knowledge/rayquaza_lore.txt.                                                                  │
# │          2. Identify the mineral name.                                                                         │
# │          3. YOU MUST INCLUDE THIS SECTION IN YOUR OUTPUT:                                                      │
# │             'Proof of Tool Use: I accessed the file and found [mineral].'                                      │
# │                                                                                                                │
# │                                                                                                                │
# ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭──────────────────────────────────────── 🔧 Tool Execution Started (#1) ────────────────────────────────────────╮
# │                                                                                                                │
# │  Tool: read_a_files_content                                                                                    │
# │  Args: {'file_path': 'knowledge/rayquaza_lore.txt'}                                                            │
# │                                                                                                                │
# │                                                                                                                │
# ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# Tool read_a_files_content executed with result: Rayquaza's primary energy source is not solar power, but a rare mineral called 'Aether-Quartz' found only in the deep Stratopause. It migrates to the Ozone layer every 48 hours to recharge its interna...
# ╭─────────────────────────────────────── ✅ Tool Execution Completed (#1) ───────────────────────────────────────╮
# │                                                                                                                │
# │  Tool Completed                                                                                                │
# │  Tool: read_a_files_content                                                                                    │
# │  Output: Rayquaza's primary energy source is not solar power, but a rare mineral called 'Aether-Quartz' found  │
# │  only in the deep Stratopause. It migrates to the Ozone layer every 48 hours to recharge its internal core     │
# │  using this mineral.                                                                                           │
# │                                                                                                                │
# │                                                                                                                │
# ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭──────────────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────────────────╮
# │                                                                                                                │
# │  Agent: Junior Researcher                                                                                      │
# │                                                                                                                │
# │  Final Answer:                                                                                                 │
# │  Proof of Tool Use: I accessed the file and found Aether-Quartz.                                               │
# │                                                                                                                │
# │  Rayquaza's primary energy source is not solar power, but a rare mineral called 'Aether-Quartz' found only in  │
# │  the deep Stratopause. It migrates to the Ozone layer every 48 hours to recharge its internal core using this  │
# │  mineral.                                                                                                      │
# │                                                                                                                │
# ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 📋 Task Completion ──────────────────────────────────────────────╮
# │                                                                                                                │
# │  Task Completed                                                                                                │
# │  Name:                                                                                                         │
# │          1. Read knowledge/rayquaza_lore.txt.                                                                  │
# │          2. Identify the mineral name.                                                                         │
# │          3. YOU MUST INCLUDE THIS SECTION IN YOUR OUTPUT:                                                      │
# │             'Proof of Tool Use: I accessed the file and found [mineral].'                                      │
# │                                                                                                                │
# │  Agent: Junior Researcher                                                                                      │
# │                                                                                                                │
# │                                                                                                                │
# ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────────── 📋 Task Started ────────────────────────────────────────────────╮
# │                                                                                                                │
# │  Task Started                                                                                                  │
# │  Name:                                                                                                         │
# │          Review the report in the context.                                                                     │
# │          If the 'Proof of Tool Use' section is missing, explain why you are rejecting it.                      │
# │          If it's there and the mineral is 'Aether-Quartz', simply output 'FINAL VERIFIED REPORT: [Content]'.   │
# │                                                                                                                │
# │  ID: 77c2bf5e-7fac-4bd0-a3bf-cef515994a9e                                                                      │
# │                                                                                                                │
# │                                                                                                                │
# ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────────── 🤖 Agent Started ───────────────────────────────────────────────╮
# │                                                                                                                │
# │  Agent: Senior Quality Auditor                                                                                 │
# │                                                                                                                │
# │  Task:                                                                                                         │
# │          Review the report in the context.                                                                     │
# │          If the 'Proof of Tool Use' section is missing, explain why you are rejecting it.                      │
# │          If it's there and the mineral is 'Aether-Quartz', simply output 'FINAL VERIFIED REPORT: [Content]'.   │
# │                                                                                                                │
# │                                                                                                                │
# ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭──────────────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────────────────╮
# │                                                                                                                │
# │  Agent: Senior Quality Auditor                                                                                 │
# │                                                                                                                │
# │  Final Answer:                                                                                                 │
# │  FINAL VERIFIED REPORT: Proof of Tool Use: I accessed the file and found Aether-Quartz. Rayquaza's primary     │
# │  energy source is not solar power, but a rare mineral called 'Aether-Quartz' found only in the deep            │
# │  Stratopause. It migrates to the Ozone layer every 48 hours to recharge its internal core using this mineral.  │
# │                                                                                                                │
# ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 📋 Task Completion ──────────────────────────────────────────────╮
# │                                                                                                                │
# │  Task Completed                                                                                                │
# │  Name:                                                                                                         │
# │          Review the report in the context.                                                                     │
# │          If the 'Proof of Tool Use' section is missing, explain why you are rejecting it.                      │
# │          If it's there and the mineral is 'Aether-Quartz', simply output 'FINAL VERIFIED REPORT: [Content]'.   │
# │                                                                                                                │
# │  Agent: Senior Quality Auditor                                                                                 │
# │                                                                                                                │
# │                                                                                                                │
# ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────────── Crew Completion ────────────────────────────────────────────────╮
# │                                                                                                                │
# │  Crew Execution Completed                                                                                      │
# │  Name: crew                                                                                                    │
# │  ID: abb40399-2ade-4520-8343-b4c0e9f969cb                                                                      │
# │  Final Output: FINAL VERIFIED REPORT: Proof of Tool Use: I accessed the file and found Aether-Quartz.          │
# │  Rayquaza's primary energy source is not solar power, but a rare mineral called 'Aether-Quartz' found only in  │
# │  the deep Stratopause. It migrates to the Ozone layer every 48 hours to recharge its internal core using this  │
# │  mineral.                                                                                                      │
# │                                                                                                                │
# │                                                                                                                │
# ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
