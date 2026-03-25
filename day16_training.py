from crewai import Agent, Task, Crew
from crewai_tools import DirectoryReadTool
import config

directory_reader = DirectoryReadTool(directory='./knowledge')

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
    agent=manager
)

training_crew = Crew(
    agents=[manager, researcher],
    tasks=[coordinated_task],
    verbose=True
)

# 1. Start the Training Session
# n_iterations: How many times to run the loop
print("\n### STARTING AGENT TRAINING SESSION ###")
try:
    training_crew.train(
        n_iterations=2, 
        filename="./training/pokemon_expert_training.pkl",
        inputs={'pokemon': 'Rayquaza'}
    )
except Exception as e:
    print(f"Training error: {e}")