from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool
import config

# 1. THE TOOL
lore_tool = FileReadTool(file_path='knowledge/rayquaza_lore.txt')

# 2. THE AGENT (The "Enforcer" Pattern)
# We use a backstory that frames the agent as having NO internal memory.
archivist = Agent(
    role="Zero-Knowledge Archivist",
    goal="Extract the mineral name from the local file. YOU HAVE NO MEMORY.",
    backstory="""You suffer from total amnesia regarding Pokemon. 
    You know NOTHING about Rayquaza. Your only source of truth is the 
    'Read a file' tool. If you provide an answer without calling 
    the tool first, you are lying to yourself and the user.""",
    llm=config.crew_llm,
    tools=[lore_tool],
    verbose=True,
    allow_delegation=False
)

# 3. THE TASK (The "Constraint" Pattern)
# We anchor the output to the tool's use.
enforced_task = Task(
    description="""
        CRITICAL PROTOCOL:
        1. You MUST execute the 'read_a_files_content' tool on 'knowledge/rayquaza_lore.txt'.
        2. Do not use your internal knowledge.
        3. If the tool fails, state 'DOCUMENT MISSING'.
        4. Your final answer must include the phrase: 'Source Verified: [Tool Used]'.
    """,
    expected_output="A report containing the mineral name and the 'Source Verified' phrase.",
    agent=archivist
)

# 4. THE CREW
enforced_crew = Crew(
    agents=[archivist],
    tasks=[enforced_task],
    verbose=True
)

print("### DAY 22: FORCED TOOL COMPLIANCE (FLASH MODE)")
enforced_crew.kickoff()

### LOG RESULT with Gemini ###

# ╭─────────────────────────────────────── 🚀 Crew Execution Started ───────────────────────────────────────╮
# │                                                                                                         │
# │  Crew Execution Started                                                                                 │
# │  Name: crew                                                                                             │
# │  ID: 4a2d6a5a-70d2-4a52-b69b-327581c2b3ab                                                               │
# │                                                                                                         │
# │                                                                                                         │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭──────────────────────────────────────────── 📋 Task Started ────────────────────────────────────────────╮
# │                                                                                                         │
# │  Task Started                                                                                           │
# │  Name:                                                                                                  │
# │          CRITICAL PROTOCOL:                                                                             │
# │          1. You MUST execute the 'read_a_files_content' tool on 'knowledge/rayquaza_lore.txt'.          │
# │          2. Do not use your internal knowledge.                                                         │
# │          3. If the tool fails, state 'DOCUMENT MISSING'.                                                │
# │          4. Your final answer must include the phrase: 'Source Verified: [Tool Used]'.                  │
# │                                                                                                         │
# │  ID: ca9b1aaa-df19-423c-9471-6f379bd8781d                                                               │
# │                                                                                                         │
# │                                                                                                         │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────╮
# │                                                                                                         │
# │  Agent: Zero-Knowledge Archivist                                                                        │
# │                                                                                                         │
# │  Task:                                                                                                  │
# │          CRITICAL PROTOCOL:                                                                             │
# │          1. You MUST execute the 'read_a_files_content' tool on 'knowledge/rayquaza_lore.txt'.          │
# │          2. Do not use your internal knowledge.                                                         │
# │          3. If the tool fails, state 'DOCUMENT MISSING'.                                                │
# │          4. Your final answer must include the phrase: 'Source Verified: [Tool Used]'.                  │
# │                                                                                                         │
# │                                                                                                         │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭──────────────────────────────────── 🔧 Tool Execution Started (#1) ─────────────────────────────────────╮
# │                                                                                                         │
# │  Tool: read_a_files_content                                                                             │
# │  Args: {'file_path': 'knowledge/rayquaza_lore.txt'}                                                     │
# │                                                                                                         │
# │                                                                                                         │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# Tool read_a_files_content executed with result: Rayquaza's primary energy source is not solar power, but a rare mineral called 'Aether-Quartz' found only in the deep Stratopause. It migrates to the Ozone layer every 48 hours to recharge its interna...
# ╭─────────────────────────────────── ✅ Tool Execution Completed (#1) ────────────────────────────────────╮
# │                                                                                                         │
# │  Tool Completed                                                                                         │
# │  Tool: read_a_files_content                                                                             │
# │  Output: Rayquaza's primary energy source is not solar power, but a rare mineral called                 │
# │  'Aether-Quartz' found only in the deep Stratopause. It migrates to the Ozone layer every 48 hours to   │
# │  recharge its internal core using this mineral.                                                         │
# │                                                                                                         │
# │                                                                                                         │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────────────╮
# │                                                                                                         │
# │  Agent: Zero-Knowledge Archivist                                                                        │
# │                                                                                                         │
# │  Final Answer:                                                                                          │
# │  Rayquaza's primary energy source is not solar power, but a rare mineral called 'Aether-Quartz' found   │
# │  only in the deep Stratopause. It migrates to the Ozone layer every 48 hours to recharge its internal   │
# │  core using this mineral. Source Verified: read_a_files_content                                         │
# │                                                                                                         │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────── 📋 Task Completion ───────────────────────────────────────────╮
# │                                                                                                         │
# │  Task Completed                                                                                         │
# │  Name:                                                                                                  │
# │          CRITICAL PROTOCOL:                                                                             │
# │          1. You MUST execute the 'read_a_files_content' tool on 'knowledge/rayquaza_lore.txt'.          │
# │          2. Do not use your internal knowledge.                                                         │
# │          3. If the tool fails, state 'DOCUMENT MISSING'.                                                │
# │          4. Your final answer must include the phrase: 'Source Verified: [Tool Used]'.                  │
# │                                                                                                         │
# │  Agent: Zero-Knowledge Archivist                                                                        │
# │                                                                                                         │
# │                                                                                                         │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭──────────────────────────────────────────── Crew Completion ────────────────────────────────────────────╮
# │                                                                                                         │
# │  Crew Execution Completed                                                                               │
# │  Name: crew                                                                                             │
# │  ID: 4a2d6a5a-70d2-4a52-b69b-327581c2b3ab                                                               │
# │  Final Output: Rayquaza's primary energy source is not solar power, but a rare mineral called           │
# │  'Aether-Quartz' found only in the deep Stratopause. It migrates to the Ozone layer every 48 hours to   │
# │  recharge its internal core using this mineral. Source Verified: read_a_files_content                   │
# │                                                                                                         │
# │                                                                                                         │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
