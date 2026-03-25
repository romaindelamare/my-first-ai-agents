from crewai import Agent, Task, Crew
import config
from pydantic import BaseModel
from typing import List

class MineralInfo(BaseModel):
    pokemon: str
    mineral_name: str
    location: str

class ExpeditionReport(BaseModel):
    findings: List[MineralInfo]
    summary: str

analyst = Agent(
    role='Data Architect',
    goal='Format expedition data into valid JSON structures.',
    backstory='You translate raw researcher notes into machine-readable data.',
    llm=config.crew_llm,
    verbose=True
)

json_task = Task(
    description="""
        Analyze the previous research on Rayquaza and Kyogre.
        Extract the mineral name and location for each.
    """,
    expected_output='A structured JSON object containing the mineral findings.',
    agent=analyst,
    output_json=ExpeditionReport 
)

output_crew = Crew(
    agents=[analyst],
    tasks=[json_task],
    verbose=True
)

result = output_crew.kickoff()

print("\n--- VALIDATED JSON OUTPUT ---")
print(result.json)

### LOG RESULT with Gemini ###
# --- VALIDATED JSON OUTPUT ---
# {"findings": [{"pokemon": "Rayquaza", "mineral_name": "Sky Stone", "location": "Sky Pillar"}, {"pokemon": "Kyogre", "mineral_name": "Deep Sea Ore", "location": "Seafloor Cavern"}], "summary": "Analysis of known habitats and lore for Rayquaza and Kyogre to identify associated minerals and locations."}