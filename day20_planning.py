from crewai import Agent, Task, Crew
import config

# 1. THE AGENTS
researcher = Agent(
    role="Lead Researcher",
    goal="Extract all technical data for {pokemon}.",
    backstory="You are focused on raw data and stats.",
    llm=config.crew_llm
)

writer = Agent(
    role="Technical Writer",
    goal="Create a professional PDF-ready report.",
    backstory="You translate raw stats into beautiful documentation.",
    llm=config.crew_llm
)

# 2. THE TASKS
task1 = Task(
    description="Analyze the base stats and evolution chain of {pokemon}.",
    expected_output="A structured list of stats and evolution requirements.",
    agent=researcher
)

task2 = Task(
    description="Write a comprehensive guide for trainers on how to use {pokemon} in competitive play.",
    expected_output="A 3-paragraph competitive guide.",
    agent=writer
)

# 3. THE CREW (With Planning Enabled)
planning_crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True,
    planning=True, 
    planning_llm=config.crew_llm 
)

print("### Running Day 20: Strategic Planning")
result = planning_crew.kickoff(inputs={'pokemon': 'Garchomp'})

print("\n--- FINAL STRATEGIC REPORT ---")
print(result)

### LOG RESULT with Gemini ###

# ### Running Day 20: Strategic Planning
# ╭───────────────────────────────────────── 🚀 Crew Execution Started ──────────────────────────────────────────╮
# │                                                                                                              │
# │  Crew Execution Started                                                                                      │
# │  Name: crew                                                                                                  │
# │  ID: 1f35834b-2ab3-48eb-a870-ec32c9064c3d                                                                    │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# 
# [2026-03-29 10:13:40][INFO]: Planning the crew execution
# ╭────────────────────────────────────────────── 📋 Task Started ───────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Started                                                                                                │
# │  Name: Based on these tasks summary:                                                                         │
# │                  Task Number 1 - Analyze the base stats and evolution chain of Garchomp.                     │
# │                  "task_description": Analyze the base stats and evolution chain of Garchomp.                 │
# │                  "task_expected_output": A structured list of stats and evolution requirements.              │
# │                  "agent": Lead Researcher                                                                    │
# │                  "agent_goal": Extract all technical data for Garchomp.                                      │
# │                  "task_tools": []                                                                            │
# │                  "agent_tools": "agent has no tools"                                                         │
# │                  Task Number 2 - Write a comprehensive guide for trainers on how to use Garchomp in          │
# │  competitive play.                                                                                           │
# │                  "task_description": Write a comprehensive guide for trainers on how to use Garchomp in      │
# │  competitive play.                                                                                           │
# │                  "task_expected_output": A 3-paragraph competitive guide.                                    │
# │                  "agent": Technical Writer                                                                   │
# │                  "agent_goal": Create a professional PDF-ready report.                                       │
# │                  "task_tools": []                                                                            │
# │                  "agent_tools": "agent has no tools"                                                         │
# │   Create the most descriptive plan based on the tasks descriptions, tools available, and agents' goals for   │
# │  them to execute their goals with perfection.                                                                │
# │  ID: 370ee72e-2405-4726-bcdc-63bd785ba04c                                                                    │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────── 📋 Task Completion ─────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Completed                                                                                              │
# │  Name: Based on these tasks summary:                                                                         │
# │                  Task Number 1 - Analyze the base stats and evolution chain of Garchomp.                     │
# │                  "task_description": Analyze the base stats and evolution chain of Garchomp.                 │
# │                  "task_expected_output": A structured list of stats and evolution requirements.              │
# │                  "agent": Lead Researcher                                                                    │
# │                  "agent_goal": Extract all technical data for Garchomp.                                      │
# │                  "task_tools": []                                                                            │
# │                  "agent_tools": "agent has no tools"                                                         │
# │                  Task Number 2 - Write a comprehensive guide for trainers on how to use Garchomp in          │
# │  competitive play.                                                                                           │
# │                  "task_description": Write a comprehensive guide for trainers on how to use Garchomp in      │
# │  competitive play.                                                                                           │
# │                  "task_expected_output": A 3-paragraph competitive guide.                                    │
# │                  "agent": Technical Writer                                                                   │
# │                  "agent_goal": Create a professional PDF-ready report.                                       │
# │                  "task_tools": []                                                                            │
# │                  "agent_tools": "agent has no tools"                                                         │
# │   Create the most descriptive plan based on the tasks descriptions, tools available, and agents' goals for   │
# │  them to execute their goals with perfection.                                                                │
# │  Agent: Task Execution Planner                                                                               │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 📋 Task Started ───────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Started                                                                                                │
# │  Name: Analyze the base stats and evolution chain of Garchomp.1. **Understand Garchomp's Core Identity**:    │
# │  Begin by recognizing Garchomp as a pseudo-legendary Dragon/Ground-type Pokémon, known for its high attack   │
# │  and speed. This foundational understanding will guide the data extraction process. 2. **Comprehensive Base  │
# │  Stat Retrieval**: Identify Garchomp's base HP, Attack, Defense, Special Attack, Special Defense, and Speed  │
# │  stats. Calculate the sum of all base stats to provide an overall power indicator. 3. **Detailed Evolution   │
# │  Chain Mapping**: Identify Gible as the base form, specifying the level at which it evolves into Gabite.     │
# │  Then, identify Gabite as the middle stage, specifying the level at which it evolves into Garchomp.          │
# │  Research if Garchomp has a Mega Evolution, identifying the required item (Garchompite) and noting any       │
# │  ability changes (e.g., Sand Force). 4. **Ability Identification**: List Garchomp's standard ability (Sand   │
# │  Veil) and its hidden ability (Rough Skin), noting their effects. 5. **Type Analysis**: Clearly state        │
# │  Garchomp's primary and secondary typing (Dragon/Ground) and list its resistances, weaknesses, and           │
# │  immunities based on this typing. 6. **Data Structuring**: Organize all gathered information into a clear,   │
# │  structured list or table format, ensuring all stats are clearly labeled and the evolution chain is easy to  │
# │  follow. This will directly fulfill the 'structured list of stats and evolution requirements' expected       │
# │  output. 7. **Review and Verification**: Double-check all extracted data against reliable sources to ensure  │
# │  accuracy and completeness, confirming that all technical data for Garchomp has been meticulously            │
# │  extracted.                                                                                                  │
# │  ID: 198f6a93-7fa6-4361-9780-651c782e20e3                                                                    │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 🤖 Agent Started ──────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Lead Researcher                                                                                      │
# │                                                                                                              │
# │  Task: Analyze the base stats and evolution chain of Garchomp.1. **Understand Garchomp's Core Identity**:    │
# │  Begin by recognizing Garchomp as a pseudo-legendary Dragon/Ground-type Pokémon, known for its high attack   │
# │  and speed. This foundational understanding will guide the data extraction process. 2. **Comprehensive Base  │
# │  Stat Retrieval**: Identify Garchomp's base HP, Attack, Defense, Special Attack, Special Defense, and Speed  │
# │  stats. Calculate the sum of all base stats to provide an overall power indicator. 3. **Detailed Evolution   │
# │  Chain Mapping**: Identify Gible as the base form, specifying the level at which it evolves into Gabite.     │
# │  Then, identify Gabite as the middle stage, specifying the level at which it evolves into Garchomp.          │
# │  Research if Garchomp has a Mega Evolution, identifying the required item (Garchompite) and noting any       │
# │  ability changes (e.g., Sand Force). 4. **Ability Identification**: List Garchomp's standard ability (Sand   │
# │  Veil) and its hidden ability (Rough Skin), noting their effects. 5. **Type Analysis**: Clearly state        │
# │  Garchomp's primary and secondary typing (Dragon/Ground) and list its resistances, weaknesses, and           │
# │  immunities based on this typing. 6. **Data Structuring**: Organize all gathered information into a clear,   │
# │  structured list or table format, ensuring all stats are clearly labeled and the evolution chain is easy to  │
# │  follow. This will directly fulfill the 'structured list of stats and evolution requirements' expected       │
# │  output. 7. **Review and Verification**: Double-check all extracted data against reliable sources to ensure  │
# │  accuracy and completeness, confirming that all technical data for Garchomp has been meticulously            │
# │  extracted.                                                                                                  │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────── ✅ Agent Final Answer ────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Lead Researcher                                                                                      │
# │                                                                                                              │
# │  Final Answer:                                                                                               │
# │  **Garchomp Technical Data Report**                                                                          │
# │                                                                                                              │
# │  **1. Core Identity:**                                                                                       │
# │  *   **Classification:** Pseudo-Legendary                                                                    │
# │  *   **Primary Type:** Dragon                                                                                │
# │  *   **Secondary Type:** Ground                                                                              │
# │                                                                                                              │
# │  **2. Base Stats:**                                                                                          │
# │  *   **HP:** 108                                                                                             │
# │  *   **Attack:** 130                                                                                         │
# │  *   **Defense:** 95                                                                                         │
# │  *   **Special Attack:** 80                                                                                  │
# │  *   **Special Defense:** 85                                                                                 │
# │  *   **Speed:** 102                                                                                          │
# │  *   **Total Base Stats:** 600                                                                               │
# │                                                                                                              │
# │  **3. Evolution Chain:**                                                                                     │
# │  *   **Base Form:** Gible                                                                                    │
# │      *   **Evolves into Gabite at:** Level 24                                                                │
# │  *   **Middle Stage:** Gabite                                                                                │
# │      *   **Evolves into Garchomp at:** Level 48                                                              │
# │  *   **Mega Evolution:** Yes                                                                                 │
# │      *   **Mega Stone:** Garchompite                                                                         │
# │      *   **Mega Ability:** Sand Force (Increases the power of Ground-, Rock-, and Steel-type moves by 30%    │
# │  during a sandstorm.)                                                                                        │
# │                                                                                                              │
# │  **4. Abilities:**                                                                                           │
# │  *   **Standard Ability:** Sand Veil (Boosts evasion by 20% during a sandstorm.)                             │
# │  *   **Hidden Ability:** Rough Skin (Damages opposing Pokémon by 1/8th of their maximum HP when they make    │
# │  contact with Garchomp.)                                                                                     │
# │                                                                                                              │
# │  **5. Type Effectiveness (Dragon/Ground):**                                                                  │
# │  *   **Resistances (0.5x Damage):**                                                                          │
# │      *   Fire                                                                                                │
# │      *   Poison                                                                                              │
# │      *   Rock                                                                                                │
# │  *   **Weaknesses (2x Damage):**                                                                             │
# │      *   Water                                                                                               │
# │      *   Grass                                                                                               │
# │      *   Dragon                                                                                              │
# │      *   Fairy                                                                                               │
# │  *   **Major Weakness (4x Damage):**                                                                         │
# │      *   Ice                                                                                                 │
# │  *   **Immunities (0x Damage):**                                                                             │
# │      *   Electric                                                                                            │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────── 📋 Task Completion ─────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Completed                                                                                              │
# │  Name: Analyze the base stats and evolution chain of Garchomp.1. **Understand Garchomp's Core Identity**:    │
# │  Begin by recognizing Garchomp as a pseudo-legendary Dragon/Ground-type Pokémon, known for its high attack   │
# │  and speed. This foundational understanding will guide the data extraction process. 2. **Comprehensive Base  │
# │  Stat Retrieval**: Identify Garchomp's base HP, Attack, Defense, Special Attack, Special Defense, and Speed  │
# │  stats. Calculate the sum of all base stats to provide an overall power indicator. 3. **Detailed Evolution   │
# │  Chain Mapping**: Identify Gible as the base form, specifying the level at which it evolves into Gabite.     │
# │  Then, identify Gabite as the middle stage, specifying the level at which it evolves into Garchomp.          │
# │  Research if Garchomp has a Mega Evolution, identifying the required item (Garchompite) and noting any       │
# │  ability changes (e.g., Sand Force). 4. **Ability Identification**: List Garchomp's standard ability (Sand   │
# │  Veil) and its hidden ability (Rough Skin), noting their effects. 5. **Type Analysis**: Clearly state        │
# │  Garchomp's primary and secondary typing (Dragon/Ground) and list its resistances, weaknesses, and           │
# │  immunities based on this typing. 6. **Data Structuring**: Organize all gathered information into a clear,   │
# │  structured list or table format, ensuring all stats are clearly labeled and the evolution chain is easy to  │
# │  follow. This will directly fulfill the 'structured list of stats and evolution requirements' expected       │
# │  output. 7. **Review and Verification**: Double-check all extracted data against reliable sources to ensure  │
# │  accuracy and completeness, confirming that all technical data for Garchomp has been meticulously            │
# │  extracted.                                                                                                  │
# │  Agent: Lead Researcher                                                                                      │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 📋 Task Started ───────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Started                                                                                                │
# │  Name: Write a comprehensive guide for trainers on how to use Garchomp in competitive play.1. **Receive and  │
# │  Review Technical Data**: Await the structured list of Garchomp's base stats, evolution chain, abilities,    │
# │  and typing from the Lead Researcher. Thoroughly review this data to understand Garchomp's fundamental       │
# │  characteristics. 2. **Outline the 3-Paragraph Guide Structure**: Define the focus for each paragraph:       │
# │  Paragraph 1 will introduce Garchomp's role and strengths, Paragraph 2 will detail strategic application     │
# │  and moveset suggestions, and Paragraph 3 will cover counterplay, synergies, and advanced tips. 3. **Draft   │
# │  Paragraph 1 - Role and Strengths**: Write an engaging opening paragraph introducing Garchomp as a dominant  │
# │  force in competitive play, emphasizing its raw power, speed, and dual STAB (Same-Type Attack Bonus) from    │
# │  its Dragon/Ground typing. Mention how its abilities contribute to its survivability or damage output. 4.    │
# │  **Draft Paragraph 2 - Strategic Application**: Construct the second paragraph focusing on practical         │
# │  competitive advice. Provide concrete examples of common competitive movesets (e.g., Swords Dance,           │
# │  Earthquake, Outrage/Dragon Claw, Stone Edge/Fire Fang), suitable held items (e.g., Choice Scarf, Choice     │
# │  Band, Life Orb, Yache Berry), and optimal EV spreads. Explain the reasoning behind these choices to         │
# │  maximize Garchomp's offensive pressure or defensive utility. 5. **Draft Paragraph 3 - Counterplay and       │
# │  Synergy**: Develop the third paragraph to offer a well-rounded perspective, acknowledging Garchomp's        │
# │  vulnerabilities (e.g., Ice-type moves, Fairy-type Pokémon) and providing solutions (e.g., team support,     │
# │  switching). Suggest synergistic teammates that complement Garchomp's strengths or cover its weaknesses.     │
# │  Include advanced tips like weather synergy (Sand Rush from other Pokémon) or specific match-up              │
# │  considerations. 6. **Review for Cohesion, Clarity, and Tone**: Ensure a smooth flow between paragraphs,     │
# │  verify that the language is clear, concise, and easy for trainers to understand, and maintain a             │
# │  professional, informative, and authoritative tone suitable for a competitive guide. Confirm that all        │
# │  aspects of a 'comprehensive guide' are covered within the 3-paragraph structure. 7. **Proofread and         │
# │  Edit**: Scrutinize the entire guide for any grammatical errors, spelling mistakes, punctuation issues, or   │
# │  awkward phrasing. Ensure the language is polished and professional, ready for a 'PDF-ready report'          │
# │  standard. 8. **Final Output Generation**: Produce the final 3-paragraph competitive guide, ensuring it      │
# │  adheres to the quality standards for a professional report.                                                 │
# │  ID: 320802a8-baec-4a83-aee9-7d8296dc3275                                                                    │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 🤖 Agent Started ──────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Technical Writer                                                                                     │
# │                                                                                                              │
# │  Task: Write a comprehensive guide for trainers on how to use Garchomp in competitive play.1. **Receive and  │
# │  Review Technical Data**: Await the structured list of Garchomp's base stats, evolution chain, abilities,    │
# │  and typing from the Lead Researcher. Thoroughly review this data to understand Garchomp's fundamental       │
# │  characteristics. 2. **Outline the 3-Paragraph Guide Structure**: Define the focus for each paragraph:       │
# │  Paragraph 1 will introduce Garchomp's role and strengths, Paragraph 2 will detail strategic application     │
# │  and moveset suggestions, and Paragraph 3 will cover counterplay, synergies, and advanced tips. 3. **Draft   │
# │  Paragraph 1 - Role and Strengths**: Write an engaging opening paragraph introducing Garchomp as a dominant  │
# │  force in competitive play, emphasizing its raw power, speed, and dual STAB (Same-Type Attack Bonus) from    │
# │  its Dragon/Ground typing. Mention how its abilities contribute to its survivability or damage output. 4.    │
# │  **Draft Paragraph 2 - Strategic Application**: Construct the second paragraph focusing on practical         │
# │  competitive advice. Provide concrete examples of common competitive movesets (e.g., Swords Dance,           │
# │  Earthquake, Outrage/Dragon Claw, Stone Edge/Fire Fang), suitable held items (e.g., Choice Scarf, Choice     │
# │  Band, Life Orb, Yache Berry), and optimal EV spreads. Explain the reasoning behind these choices to         │
# │  maximize Garchomp's offensive pressure or defensive utility. 5. **Draft Paragraph 3 - Counterplay and       │
# │  Synergy**: Develop the third paragraph to offer a well-rounded perspective, acknowledging Garchomp's        │
# │  vulnerabilities (e.g., Ice-type moves, Fairy-type Pokémon) and providing solutions (e.g., team support,     │
# │  switching). Suggest synergistic teammates that complement Garchomp's strengths or cover its weaknesses.     │
# │  Include advanced tips like weather synergy (Sand Rush from other Pokémon) or specific match-up              │
# │  considerations. 6. **Review for Cohesion, Clarity, and Tone**: Ensure a smooth flow between paragraphs,     │
# │  verify that the language is clear, concise, and easy for trainers to understand, and maintain a             │
# │  professional, informative, and authoritative tone suitable for a competitive guide. Confirm that all        │
# │  aspects of a 'comprehensive guide' are covered within the 3-paragraph structure. 7. **Proofread and         │
# │  Edit**: Scrutinize the entire guide for any grammatical errors, spelling mistakes, punctuation issues, or   │
# │  awkward phrasing. Ensure the language is polished and professional, ready for a 'PDF-ready report'          │
# │  standard. 8. **Final Output Generation**: Produce the final 3-paragraph competitive guide, ensuring it      │
# │  adheres to the quality standards for a professional report.                                                 │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────── ✅ Agent Final Answer ────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Technical Writer                                                                                     │
# │                                                                                                              │
# │  Final Answer:                                                                                               │
# │  **Garchomp: The Apex Predator's Guide to Competitive Dominance**                                            │
# │                                                                                                              │
# │  Garchomp stands as a formidable force in competitive play, leveraging its impressive base stat total of     │
# │  600, highlighted by a staggering 130 Attack and a swift 102 Speed, to exert immense offensive pressure.     │
# │  Its unique Dragon/Ground typing grants it powerful dual STAB (Same-Type Attack Bonus) coverage, hitting a   │
# │  vast array of Pokémon for super-effective damage while boasting crucial resistances to Fire, Poison, and    │
# │  Rock, and a complete immunity to Electric-type attacks. Furthermore, its abilities enhance its battlefield  │
# │  presence: Sand Veil offers a chance to evade attacks in a sandstorm, while Rough Skin punishes contact      │
# │  moves, chipping away at opposing Pokémon's health, making Garchomp a threat even when taking hits. This     │
# │  potent combination of raw power, blazing speed, and strategic typing solidifies Garchomp's role as a        │
# │  premier offensive pivot, wallbreaker, or late-game cleaner.                                                 │
# │                                                                                                              │
# │  To maximize Garchomp's impact, trainers often employ tailored strategies. A common and highly effective     │
# │  offensive moveset includes Swords Dance to boost its already fearsome Attack, paired with Earthquake as     │
# │  its primary Ground STAB, and Outrage or Dragon Claw for Dragon STAB. For coverage, Stone Edge offers a      │
# │  crucial answer to Flying and Ice types, while Fire Fang can deter Steel-types like Ferrothorn. Optimal      │
# │  held items often include Choice Scarf to outspeed critical threats, Choice Band for unparalleled damage     │
# │  output, or Life Orb for a consistent power boost across multiple moves. The Yache Berry is also a valuable  │
# │  defensive option, halving the damage from an otherwise devastating Ice-type attack. For EV spreads, a       │
# │  standard 252 Attack / 4 Defense / 252 Speed ensures maximum offensive potential, though careful trainers    │
# │  might allocate EVs into HP or Defense to improve survivability against specific threats.                    │
# │                                                                                                              │
# │  Despite its strengths, Garchomp does possess exploitable weaknesses that competitive trainers must          │
# │  address. Its 4x weakness to Ice-type attacks and 2x weaknesses to Fairy, Water, Grass, and Dragon-type      │
# │  moves necessitate careful positioning and team support. Fairy-types, in particular, can safely switch into  │
# │  Garchomp's Dragon STAB. Effective counterplay involves scouting for these threats and switching into        │
# │  appropriate teammates. Synergistic partners like Steel-types (e.g., Corviknight, Ferrothorn) can reliably   │
# │  switch into Ice and Fairy attacks, while Fire-types (e.g., Volcarona, Heatran) resist Fairy and Ice,        │
# │  covering Garchomp's vulnerabilities. Advanced strategies might involve pairing Garchomp with Pokémon that   │
# │  set up sandstorms, such as Hippowdon or Tyranitar, to activate its Sand Veil ability for increased          │
# │  evasion, or to boost a potential Mega Garchomp's Sand Force ability. Understanding these match-ups and      │
# │  leveraging team support are paramount to unleashing Garchomp's full potential as an undisputed competitive  │
# │  juggernaut.                                                                                                 │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────── 📋 Task Completion ─────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Completed                                                                                              │
# │  Name: Write a comprehensive guide for trainers on how to use Garchomp in competitive play.1. **Receive and  │
# │  Review Technical Data**: Await the structured list of Garchomp's base stats, evolution chain, abilities,    │
# │  and typing from the Lead Researcher. Thoroughly review this data to understand Garchomp's fundamental       │
# │  characteristics. 2. **Outline the 3-Paragraph Guide Structure**: Define the focus for each paragraph:       │
# │  Paragraph 1 will introduce Garchomp's role and strengths, Paragraph 2 will detail strategic application     │
# │  and moveset suggestions, and Paragraph 3 will cover counterplay, synergies, and advanced tips. 3. **Draft   │
# │  Paragraph 1 - Role and Strengths**: Write an engaging opening paragraph introducing Garchomp as a dominant  │
# │  force in competitive play, emphasizing its raw power, speed, and dual STAB (Same-Type Attack Bonus) from    │
# │  its Dragon/Ground typing. Mention how its abilities contribute to its survivability or damage output. 4.    │
# │  **Draft Paragraph 2 - Strategic Application**: Construct the second paragraph focusing on practical         │
# │  competitive advice. Provide concrete examples of common competitive movesets (e.g., Swords Dance,           │
# │  Earthquake, Outrage/Dragon Claw, Stone Edge/Fire Fang), suitable held items (e.g., Choice Scarf, Choice     │
# │  Band, Life Orb, Yache Berry), and optimal EV spreads. Explain the reasoning behind these choices to         │
# │  maximize Garchomp's offensive pressure or defensive utility. 5. **Draft Paragraph 3 - Counterplay and       │
# │  Synergy**: Develop the third paragraph to offer a well-rounded perspective, acknowledging Garchomp's        │
# │  vulnerabilities (e.g., Ice-type moves, Fairy-type Pokémon) and providing solutions (e.g., team support,     │
# │  switching). Suggest synergistic teammates that complement Garchomp's strengths or cover its weaknesses.     │
# │  Include advanced tips like weather synergy (Sand Rush from other Pokémon) or specific match-up              │
# │  considerations. 6. **Review for Cohesion, Clarity, and Tone**: Ensure a smooth flow between paragraphs,     │
# │  verify that the language is clear, concise, and easy for trainers to understand, and maintain a             │
# │  professional, informative, and authoritative tone suitable for a competitive guide. Confirm that all        │
# │  aspects of a 'comprehensive guide' are covered within the 3-paragraph structure. 7. **Proofread and         │
# │  Edit**: Scrutinize the entire guide for any grammatical errors, spelling mistakes, punctuation issues, or   │
# │  awkward phrasing. Ensure the language is polished and professional, ready for a 'PDF-ready report'          │
# │  standard. 8. **Final Output Generation**: Produce the final 3-paragraph competitive guide, ensuring it      │
# │  adheres to the quality standards for a professional report.                                                 │
# │  Agent: Technical Writer                                                                                     │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── Crew Completion ───────────────────────────────────────────────╮
# │                                                                                                              │
# │  Crew Execution Completed                                                                                    │
# │  Name: crew                                                                                                  │
# │  ID: 1f35834b-2ab3-48eb-a870-ec32c9064c3d                                                                    │
# │  Final Output: **Garchomp: The Apex Predator's Guide to Competitive Dominance**                              │
# │                                                                                                              │
# │  Garchomp stands as a formidable force in competitive play, leveraging its impressive base stat total of     │
# │  600, highlighted by a staggering 130 Attack and a swift 102 Speed, to exert immense offensive pressure.     │
# │  Its unique Dragon/Ground typing grants it powerful dual STAB (Same-Type Attack Bonus) coverage, hitting a   │
# │  vast array of Pokémon for super-effective damage while boasting crucial resistances to Fire, Poison, and    │
# │  Rock, and a complete immunity to Electric-type attacks. Furthermore, its abilities enhance its battlefield  │
# │  presence: Sand Veil offers a chance to evade attacks in a sandstorm, while Rough Skin punishes contact      │
# │  moves, chipping away at opposing Pokémon's health, making Garchomp a threat even when taking hits. This     │
# │  potent combination of raw power, blazing speed, and strategic typing solidifies Garchomp's role as a        │
# │  premier offensive pivot, wallbreaker, or late-game cleaner.                                                 │
# │                                                                                                              │
# │  To maximize Garchomp's impact, trainers often employ tailored strategies. A common and highly effective     │
# │  offensive moveset includes Swords Dance to boost its already fearsome Attack, paired with Earthquake as     │
# │  its primary Ground STAB, and Outrage or Dragon Claw for Dragon STAB. For coverage, Stone Edge offers a      │
# │  crucial answer to Flying and Ice types, while Fire Fang can deter Steel-types like Ferrothorn. Optimal      │
# │  held items often include Choice Scarf to outspeed critical threats, Choice Band for unparalleled damage     │
# │  output, or Life Orb for a consistent power boost across multiple moves. The Yache Berry is also a valuable  │
# │  defensive option, halving the damage from an otherwise devastating Ice-type attack. For EV spreads, a       │
# │  standard 252 Attack / 4 Defense / 252 Speed ensures maximum offensive potential, though careful trainers    │
# │  might allocate EVs into HP or Defense to improve survivability against specific threats.                    │
# │                                                                                                              │
# │  Despite its strengths, Garchomp does possess exploitable weaknesses that competitive trainers must          │
# │  address. Its 4x weakness to Ice-type attacks and 2x weaknesses to Fairy, Water, Grass, and Dragon-type      │
# │  moves necessitate careful positioning and team support. Fairy-types, in particular, can safely switch into  │
# │  Garchomp's Dragon STAB. Effective counterplay involves scouting for these threats and switching into        │
# │  appropriate teammates. Synergistic partners like Steel-types (e.g., Corviknight, Ferrothorn) can reliably   │
# │  switch into Ice and Fairy attacks, while Fire-types (e.g., Volcarona, Heatran) resist Fairy and Ice,        │
# │  covering Garchomp's vulnerabilities. Advanced strategies might involve pairing Garchomp with Pokémon that   │
# │  set up sandstorms, such as Hippowdon or Tyranitar, to activate its Sand Veil ability for increased          │
# │  evasion, or to boost a potential Mega Garchomp's Sand Force ability. Understanding these match-ups and      │
# │  leveraging team support are paramount to unleashing Garchomp's full potential as an undisputed competitive  │
# │  juggernaut.                                                                                                 │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# 
# --- FINAL STRATEGIC REPORT ---
# **Garchomp: The Apex Predator's Guide to Competitive Dominance**
# 
# Garchomp stands as a formidable force in competitive play, leveraging its impressive base stat total of 600, highlighted by a staggering 130 Attack and a swift 102 Speed, to exert immense offensive pressure. Its unique Dragon/Ground typing grants it powerful dual STAB (Same-Type Attack Bonus) coverage, hitting a vast array of Pokémon for super-effective damage while boasting crucial resistances to Fire, Poison, and Rock, and a complete immunity to Electric-type attacks. Furthermore, its abilities enhance its battlefield presence: Sand Veil offers a chance to evade attacks in a sandstorm, while Rough Skin punishes contact moves, chipping away at opposing Pokémon's health, making Garchomp a threat even when taking hits. This potent combination of raw power, blazing speed, and strategic typing solidifies Garchomp's role as a premier offensive pivot, wallbreaker, or late-game cleaner.   
# 
# To maximize Garchomp's impact, trainers often employ tailored strategies. A common and highly effective offensive moveset includes Swords Dance to boost its already fearsome Attack, paired with Earthquake as its primary Ground STAB, and Outrage or Dragon Claw for Dragon STAB. For coverage, Stone Edge offers a crucial answer to Flying and Ice types, while Fire Fang can deter Steel-types like Ferrothorn. Optimal held items often include Choice Scarf to outspeed critical threats, Choice Band for unparalleled damage output, or Life Orb for a consistent power boost across multiple moves. The Yache Berry is also a valuable defensive option, halving the damage from an otherwise devastating Ice-type attack. For EV spreads, a standard 252 Attack / 4 Defense / 252 Speed ensures maximum offensive potential, though careful trainers might allocate EVs into HP or Defense to improve survivability against specific threats.
# 
# Despite its strengths, Garchomp does possess exploitable weaknesses that competitive trainers must address. Its 4x weakness to Ice-type attacks and 2x weaknesses to Fairy, Water, Grass, and Dragon-type moves necessitate careful positioning and team support. Fairy-types, in particular, can safely switch into Garchomp's Dragon STAB. Effective counterplay involves scouting for these threats and switching into appropriate teammates. Synergistic partners like Steel-types (e.g., Corviknight, Ferrothorn) can reliably switch into Ice and Fairy attacks, while Fire-types (e.g., Volcarona, Heatran) resist Fairy and Ice, covering Garchomp's vulnerabilities. Advanced strategies might involve pairing Garchomp with Pokémon that set up sandstorms, such as Hippowdon or Tyranitar, to activate its Sand Veil ability for increased evasion, or to boost a potential Mega Garchomp's Sand Force ability. Understanding these match-ups and leveraging team support are paramount to unleashing Garchomp's full potential as an undisputed competitive juggernaut.