from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool
import config

ray_tool = FileReadTool(file_path='knowledge/rayquaza_lore.txt')
kyo_tool = FileReadTool(file_path='knowledge/kyogre_lore.txt')

researcher = Agent(
    role='Sky Specialist',
    goal='Identify the mineral in the rayquaza_lore.txt file.',
    backstory="""Expert researcher. 
        IMPORTANT: When using tools, always provide the input as a simple 
        dictionary. Never use square brackets [] around your tool inputs.
        Example: {"file_path": "your_file.txt"}""",
    llm=config.crew_llm,
    tools=[ray_tool],
    verbose=True
)

analyst = Agent(
    role='Sea Specialist',
    goal='Identify the mineral in the kyogre_lore.txt file.',
    backstory="""Expert researcher. 
        IMPORTANT: When using tools, always provide the input as a simple 
        dictionary. Never use square brackets [] around your tool inputs.
        Example: {"file_path": "your_file.txt"}""",
    llm=config.crew_llm,
    tools=[kyo_tool],
    verbose=True
)

task1 = Task(
    description='Read the first 10 lines of rayquaza_lore.txt and find the mineral name.',
    expected_output='The name of the sky mineral.',
    agent=researcher,
    async_execution=True # Parallel run
)

task2 = Task(
    description='Read the first 10 lines of kyogre_lore.txt and find the mineral name.',
    expected_output='The name of the sea mineral.',
    agent=analyst,
    async_execution=True  # Parallel run
)

manager_task = Task(
    description='Summarize the findings from both the Sky and Sea specialists.',
    expected_output='A combined report of both minerals.',
    context=[task1, task2],
    agent=researcher # One of the agents can wrap it up
)

# 5. The Crew
async_crew = Crew(
    agents=[researcher, analyst],
    tasks=[task1, task2, manager_task],
    verbose=True
)

print("\n--- STARTING PARALLEL RESEARCH ---")
result = async_crew.kickoff()
print(result)

### LOG RESULT with Gemini ###
# The Sky specialist identified 'Aether-Quartz' as the mineral. The Sea specialist identified 'Hydros-Crystals' as the mineral.