######################################
# The TextFileKnowledgeSource try to call OpenAI so we will use the FileReadTool
# to read the file content and provide it to the agent as context instead of using
# a knowledge source.
# This way we can use another model source and still have the agent access the information
# from the file.
######################################
from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool
# from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from config import crew_llm, crew_embedder, storage_path

file_tool = FileReadTool(file_path='knowledge/rayquaza_lore.txt')

# Setup the Knowledge Source
# pokemon_source = TextFileKnowledgeSource(
#     file_paths=["rayquaza_lore.txt"],
#     embedder_config=crew_embedder,
#     llm=crew_llm
# )

archivist = Agent(
    role='Lead Pokemon Researcher',
    goal='Answer queries using only the provided official archives.',
    backstory="""You are a meticulous researcher. You trust your local 
    documentation above all else. If the information is in the archives, 
    use it. If not, state that the information is missing.""",
    llm=crew_llm,
    tools=[file_tool],
    verbose=True
)

research_task = Task(
    description="""
        1. Search the official archives specifically for 'energy source' and 'mineral'.
        2. Do NOT rely on your internal knowledge of Pokemon myths.
        3. If you find mention of a mineral called 'Aether-Quartz', report it immediately.
    """,
    expected_output='A report naming the mineral and its exact location.',
    agent=archivist
)

knowledge_crew = Crew(
    agents=[archivist],
    tasks=[research_task],
    #knowledge_sources=[pokemon_source], # Add source
    memory=False,
    embedder=crew_embedder,
    manager_llm=crew_llm,
    memory_config={
        "llm": crew_llm,
        "short_term_memory": {"enabled": True, "config": {"path": f"{storage_path}/short_term"}},
        "long_term_memory": {"enabled": True, "config": {"path": f"{storage_path}/long_term"}},
        "entity_memory": {"enabled": True, "config": {"path": f"{storage_path}/entity"}},
        "recall_memory": {"enabled": True, "config": {"path": f"{storage_path}/recall"}}
    },
    verbose=True
)

# Execute
print("\n--- CONSULTING THE ARCHIVES ---")
result = knowledge_crew.kickoff()
print("\n--- FINAL RESEARCH REPORT ---")
print(result)


### LOG RESULT with Ollama ###
# --- FINAL RESEARCH REPORT ---
# Rayquaza's energy source is identified as 'Aether-Quartz', a rare mineral found only in the deep Stratopause. According to the official archives, it migrates to the Ozone layer every 48 hours to recharge its internal core using this mineral.