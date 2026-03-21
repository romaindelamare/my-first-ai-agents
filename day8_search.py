from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from config import crew_llm

# 1. Initialize the Search Tool
search_tool = SerperDevTool()

# 2. GIVE THE TOOL TO THE RESEARCHER
researcher = Agent(
    role='Real-time Pokemon News Scout',
    goal='Find the latest news or stats about {pokemon} from the live web.',
    backstory='You are a digital scout with access to the entire internet.',
    tools=[search_tool], # The agent now has "hands"!
    llm=crew_llm,
    verbose=True
)

# 3. Define the Task
task_search = Task(
    description='Search the internet for 3 recent facts or news items about {pokemon}.',
    expected_output='A bulleted list of the 3 most recent facts found.',
    agent=researcher
)

# 4. Execute
crew = Crew(
    agents=[researcher],
    tasks=[task_search],
    process=Process.sequential
)

result = crew.kickoff(inputs={'pokemon': 'Pikachu'})
print(result)

### LOG RESULT with Gemini ###
# *   Gigantamax Pikachu will debut in Pokémon GO during a new Max Battle Day.
# *   Pokémon fans are desperate for the return of Pikachu's secret evolution, Gorochu.
# *   A new variant of Pikachu, called Peakychu, has been revealed, sporting a pale, white design and more reserved demeanor.