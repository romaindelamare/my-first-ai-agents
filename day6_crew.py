from crewai import Agent, Task, Crew, Process
from config import crew_llm

# 1. Define the Agent
researcher = Agent(
  role='Senior Pokemon Researcher',
  goal='Discover the hidden competitive strengths of {pokemon}',
  backstory="""You are a world-renowned Pokemon expert. 
  You specialize in finding unique battle strategies that others miss.""",
  llm=crew_llm,
  verbose=True # See the agent "thinking" in the console
)

# 2. Define the Task
research_task = Task(
  description='Analyze the competitive viability of {pokemon}. Focus on its type advantages.',
  expected_output='A 3-paragraph report on the Pokemon\'s battle potential.',
  agent=researcher
)

# 3. Form the Crew
pokemon_crew = Crew(
  agents=[researcher],
  tasks=[research_task],
  process=Process.sequential # For now, agents work one after another
)

# 4. Start the work!
result = pokemon_crew.kickoff(inputs={'pokemon': 'Charizard'})
print("### FINAL REPORT ###")
print(result)

### LOG RESULT with Gemini ###
# ### FINAL REPORT ###
# Charizard, a quintessential Fire/Flying-type, often finds itself at the forefront of competitive discussion, not just for its iconic status but for its inherent potential. While its base form might appear daunting due to well-known vulnerabilities, a deeper analysis reveals a type combination that, when leveraged correctly, provides significant offensive and defensive advantages. My research focuses on uncovering how Charizard's unique typing can dictate battle flow and create opportunities others often overlook, pushing past the common narrative to exploit its true competitive strengths.
# 
# Delving into its Fire/Flying typing, Charizard boasts a valuable offensive profile. Fire STAB (Same-Type Attack Bonus) delivers super-effective damage to Grass, Ice, Bug, and Steel types, all of which are common threats in various metagames. Complementing this, its Flying STAB hits Grass, Fighting, and Bug types for super-effective damage. This dual STAB combination offers fantastic neutral coverage against a wide array of Pokemon, ensuring that very few types can resist both its primary attacks. Defensively, Charizard benefits from key resistances: a crucial 4x resistance to Grass, along with resistances to Fighting, Bug, Steel, and Fire. These resistances allow it to switch into many prevalent attackers, particularly Grass and Fighting types, mitigating damage and immediately pivoting into an offensive stance.   
# 
# However, Charizard's primary challenge lies in its defensive type disadvantages, most notably its crippling 4x weakness to Rock, alongside vulnerabilities to Water and Electric. This makes entry hazards like Stealth Rock incredibly punishing, often limiting its longevity. Despite this, the true competitive strength of Charizard lies in its ability to force favorable offensive exchanges and maintain momentum. By carefully selecting switch-in opportunities against its resisted types, Charizard can unleash powerful STAB attacks that are super-effective against a broad range of foes. Its respectable speed tier, combined with its high Special Attack, allows it to outspeed and eliminate many threats before they can capitalize on its weaknesses. The goal is to use Charizard not as a bulky tank, but as a fast, offensive pivot that threatens specific opponents, clearing the path for its teammates and creating an advantage through precise, well-timed strikes that leverage its inherent type advantages.