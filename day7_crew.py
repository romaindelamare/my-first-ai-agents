from crewai import Agent, Task, Crew, Process
from config import crew_llm

# Define the Specialist Agents
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

# Define the Tasks
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

# 4. Assemble the Crew
pokemon_crew = Crew(
    agents=[researcher, editor],
    tasks=[task_research, task_edit],
    process=Process.sequential # Task 1 -> Task 2
)

# 5. Kickoff!
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