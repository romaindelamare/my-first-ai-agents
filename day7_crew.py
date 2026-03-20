from crewai import Agent, Task, Crew, Process
from config import crew_llm

# 1. Define the Specialist Agents
researcher = Agent(
    role='Pokemon Data Researcher',
    goal='Retrieve the official type, height, and weight for {pokemon}.',
    backstory='You are a meticulous researcher who only trusts verified Pokedex data.',
    llm=crew_llm,
    verbose=True
)

editor = Agent(
    role='Chief Scientific Editor',
    goal='Audit the research for accuracy and format it into a professional report.',
    backstory='You are a perfectionist editor. You ensure all data is consistent and clear.',
    llm=crew_llm,
    verbose=True
)

# 2. Define the Tasks
task_research = Task(
    description='Find the official stats for the Pokemon: {pokemon}.',
    expected_output='A raw list of type, height, and weight.',
    agent=researcher
)

task_edit = Task(
    description='Review the stats from the researcher. Format them into a clean Markdown table.',
    expected_output='A polished Markdown table with a brief summary.',
    agent=editor,
    context=[task_research] # This "plugs" the output of research into the editor
)

# 3. Assemble the Crew
pokemon_crew = Crew(
    agents=[researcher, editor],
    tasks=[task_research, task_edit],
    process=Process.sequential # Task 1 -> Task 2
)

# 4. Start the work!
result = pokemon_crew.kickoff(inputs={'pokemon': 'Squirtle'})
print("### FINAL OUTPUT ###")
print(result)

### LOG RESULT with Gemini ###
# ### FINAL OUTPUT ###
# The following data points have been reviewed and are presented in a clear, consistent format.
# 
# ### Research Data Summary
# 
# The table below outlines the key parameters observed for the specified substance.
# 
# | Parameter | Value   |
# | :-------- | :------ |
# | Substance | Water   |
# | Length    | 0.5 m   |
# | Mass      | 9.0 kg  |

result = pokemon_crew.kickoff(inputs={'pokemon': 'Batman'})
print("### FINAL OUTPUT ###")
print(result)

### LOG RESULT with Gemini ###
### FINAL OUTPUT ###
# **Research Audit Report: Unofficial Pokémon Data**
# 
# **Summary:**
# This report audits the provided data for "Batman" within the context of the official Pokémon universe. Our rigorous audit confirms, based on verified Pokedex data, that "Batman" is not an official Pokémon species. Consequently, there are no official type, height, or weight statistics available for this entity within the established Pokémon canon. Any purported statistics would be unofficial and speculative, falling outside the scope of authenticated Pokedex records.  
# 
# **Detailed Statistics:**
# 
# | Attribute | Value | Notes                                       |
# | :-------- | :---- | :------------------------------------------ |
# | **Name**  | Batman| Not an official Pokémon species.            |
# | **Type**  | N/A   | No official type data exists for unofficial entities. |
# | **Height**| N/A   | No official height data exists for unofficial entities. |
# | **Weight**| N/A   | No official weight data exists for unofficial entities. |