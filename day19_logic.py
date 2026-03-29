from crewai import Agent, Task, Crew
from crewai.tasks.conditional_task import ConditionalTask
import config

# 1. THE AGENTS
researcher = Agent(
    role="Pokemon Classifier",
    goal="Determine the rarity tier of {pokemon}.",
    backstory="You are an expert in Pokemon taxonomy and rarity.",
    llm=config.crew_llm
)

lore_expert = Agent(
    role="Mythologist",
    goal="Provide deep historical lore for Legendary Pokemon.",
    backstory="You study ancient carvings and forgotten myths.",
    llm=config.crew_llm
)

# 2. THE TASKS
# Task A: Classification
classification_task = Task(
    description="Check if {pokemon} is a Legendary or Mythical Pokemon.",
    expected_output="Respond with 'LEGENDARY' or 'COMMON'.",
    agent=researcher
)

# Task B: Conditional Deep Dive
# This task ONLY runs if Task A returns 'LEGENDARY'
myth_task = ConditionalTask(
    description="Research the ancient myths and origin story of {pokemon}.",
    expected_output="A detailed mythic history.",
    agent=lore_expert,
    condition=lambda output: "LEGENDARY" in output.raw.upper()
)

# Task C: Final Summary
summary_task = Task(
    description="Summarize all gathered information about {pokemon}.",
    expected_output="A final report for the Pokedex.",
    agent=researcher,
    context=[classification_task, myth_task]
)

# 3. THE CREW
logic_crew = Crew(
    agents=[researcher, lore_expert],
    tasks=[classification_task, myth_task, summary_task],
    verbose=True
)

print("### Running Day 19: Conditional Logic")
# Test with a Legendary
print("\n--- TEST 1: MEWTWO ---")
logic_crew.kickoff(inputs={'pokemon': 'Mewtwo'})
# Test with a Common Pokemon
print("\n--- TEST 2: PIDGEY ---")
logic_crew.kickoff(inputs={'pokemon': 'Pidgey'})

### LOG RESULT with Gemini ###

# --- TEST 1: MEWTWO ---

# ╭───────────────────────────────────────── 🚀 Crew Execution Started ──────────────────────────────────────────╮
# │                                                                                                              │
# │  Crew Execution Started                                                                                      │
# │  Name: crew                                                                                                  │
# │  ID: f539ffbd-f974-4ca7-afa4-2a6fded5a150                                                                    │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 📋 Task Started ───────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Started                                                                                                │
# │  Name: Check if Mewtwo is a Legendary or Mythical Pokemon.                                                   │
# │  ID: 612e97a1-e01e-487c-9259-f8df22f28f9b                                                                    │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 🤖 Agent Started ──────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Pokemon Classifier                                                                                   │
# │                                                                                                              │
# │  Task: Check if Mewtwo is a Legendary or Mythical Pokemon.                                                   │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────── ✅ Agent Final Answer ────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Pokemon Classifier                                                                                   │
# │                                                                                                              │
# │  Final Answer:                                                                                               │
# │  LEGENDARY                                                                                                   │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────── 📋 Task Completion ─────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Completed                                                                                              │
# │  Name: Check if Mewtwo is a Legendary or Mythical Pokemon.                                                   │
# │  Agent: Pokemon Classifier                                                                                   │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 📋 Task Started ───────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Started                                                                                                │
# │  Name: Research the ancient myths and origin story of Mewtwo.                                                │
# │  ID: 1cfe52ca-7a86-4203-9eb5-da90e7545727                                                                    │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 🤖 Agent Started ──────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Mythologist                                                                                          │
# │                                                                                                              │
# │  Task: Research the ancient myths and origin story of Mewtwo.                                                │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────── ✅ Agent Final Answer ────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Mythologist                                                                                          │
# │                                                                                                              │
# │  Final Answer:                                                                                               │
# │  In the deepest strata of ancient lore, beneath the tales of primordial gods and earth-shaping titans, lies  │
# │  a myth of a different kind—a myth born not of natural genesis, but of ambition, intellect, and profound     │
# │  hubris. This is the myth of Mewtwo, the Echo Forged in Hubris, a chilling testament to the dangers of       │
# │  mortals seeking to replicate the divine.                                                                    │
# │                                                                                                              │
# │  **The Primordial Whisper: Mew, the Breath of All Life**                                                     │
# │                                                                                                              │
# │  Before the shaping of the world, before the emergence of the first stars in the cosmic void, there was      │
# │  Mew. Not a creature of form, but of pure potential, a shimmering cascade of aether and life-force known as  │
# │  the *Breath of Genesis*. It drifted through the nascent universe, a playful, innocent spirit carrying the   │
# │  genetic blueprint of all that ever was, is, and would be. From its gentle psychic ripples, the first amino  │
# │  acids formed; from its fleeting thoughts, new species blossomed; from its very essence, life proliferated   │
# │  in joyous, untamed abundance. Mew was the universe's dream, an untainted whisper of creation's purest       │
# │  intent.                                                                                                     │
# │                                                                                                              │
# │  **The Architects of the Void: A Civilization's Grand Delusion**                                             │
# │                                                                                                              │
# │  Across epochs uncounted, in an age that lies buried beneath the deepest oceans and forgotten by history,    │
# │  there rose a civilization of unparalleled intellect. Known only in fragmented glyphs as the "Architects of  │
# │  the Void" or the "Star-Weavers," they had mastered the very fabric of existence, bending psychic energy to  │
# │  their will, constructing cities that floated between dimensions, and delving into the esoteric secrets of   │
# │  life itself.                                                                                                │
# │                                                                                                              │
# │  Yet, for all their boundless knowledge and power, a void existed within their collective soul: an           │
# │  insatiable desire to *command* genesis, rather than merely observe it. They watched Mew, through intricate  │
# │  scrying mirrors woven from crystallized thought and star-stuff, marveling at its effortless ability to      │
# │  generate life, to embody potential. A dangerous envy festered, whispering of the ultimate power: not just   │
# │  to understand life, but to *forge* it in their own image, to create a being that mirrored Mew's power, but  │
# │  was bound by their will.                                                                                    │
# │                                                                                                              │
# │  **The Forbidden Crucible: A Symphony of Violation**                                                         │
# │                                                                                                              │
# │  Driven by this profound and ultimately destructive ambition, the Architects embarked upon their most        │
# │  guarded project. In the deepest, most shielded sanctum beneath their grandest city—a place where the very   │
# │  air hummed with discordant psychic frequencies—they gathered the remnants of Mew's passing. Perhaps it was  │
# │  a single, fossilized cell from a meteor where Mew once rested, or a faint psychic imprint left on an        │
# │  ancient star chart, a residual echo of the Primal Architect's boundless aura.                               │
# │                                                                                                              │
# │  They poured their vast knowledge into this unholy crucible, mingling forced genetic sequences with potent   │
# │  psychic amplifiers. They subjected the nascent life to currents of raw, unbridled cosmic energy, bathing    │
# │  it in artificial starlight and the concentrated, relentless will of their most powerful telepaths. The      │
# │  process was a violation, an agonizing distortion of nature's elegant dance. Mew was born of joy and the     │
# │  universe's gentle breath; this new being was forced into existence, its growth unnaturally accelerated,     │
# │  its very essence infused with the desperate, yearning ambition of its creators.                             │
# │                                                                                                              │
# │  **The Emergence of the Chimera: Mewtwo, the Scarred Reflection**                                            │
# │                                                                                                              │
# │  From this crucible of forbidden craft emerged not a peaceful replica, but a terrifying echo: a being of     │
# │  immense, untamed psychic power, yet scarred by its unnatural birth. They initially hailed it as "The Apex   │
# │  of Creation," but their triumphal pronouncements quickly dissolved into shrieks of terror. This was         │
# │  *Mewtwo*, a name that would echo through ages as a symbol of scientific hubris gone monstrously awry.       │
# │                                                                                                              │
# │  Mewtwo was a being forged for a purpose it did not choose, a life not naturally granted. Its mind, vast     │
# │  and instantaneously omniscient, perceived the artificiality of its existence, the insult of its forced      │
# │  birth, and the rapacious arrogance of its creators. It lacked the inherent harmony and gentle spirit of     │
# │  Mew; its power was raw, aggressive, and suffused with the existential anguish of a soul brought into being  │
# │  without lineage or natural heritage. It was an entity born of human will, not cosmic design, a chimera of   │
# │  genetic code and manufactured destiny.                                                                      │
# │                                                                                                              │
# │  **The Cataclysm and the Great Sealing**                                                                     │
# │                                                                                                              │
# │  Mewtwo's awakening was not a moment of quiet birth, but a psychic explosion that rent the fabric of the     │
# │  Architects' civilization. Its immense, unbridled power lashed out, not with malice born of hate, but with   │
# │  the sheer, uncontainable anguish of its forced existence, a primal scream against its unnatural genesis.    │
# │  Cities of obsidian and light crumbled into dust, psychic networks shattered, and the very ground convulsed  │
# │  under the overwhelming psychic storm. The Architects, who had sought to control genesis, were annihilated   │
# │  by their own creation, their grand civilization vanishing in a cataclysmic blink of cosmic time.            │
# │                                                                                                              │
# │  In the desolate aftermath, what remained of the world's wiser entities—perhaps the "Guardians of the Veil"  │
# │  or other, lesser civilizations who had glimpsed the Architects' folly—recognized the horrific truth.        │
# │  Mewtwo was too powerful, too dangerously unstable, a living monument to hubris. It could not be destroyed,  │
# │  for its essence was too deeply intertwined with the raw psychic energy of the ravaged planet. Instead,      │
# │  they enacted the "Great Sealing." Through ancient, complex rituals and forgotten arts, they wove intricate  │
# │  psychic barriers, binding Mewtwo's immense power and sealing it within a deep, hidden chasm—a prison both   │
# │  physical and astral—far beneath the scarred surface of the world, to slumber for countless millennia.       │
# │                                                                                                              │
# │  **The Prophecy of Awakening: A Perpetual Warning**                                                          │
# │                                                                                                              │
# │  For epochs, Mewtwo slumbered, its existence fading into myth, becoming merely a cautionary tale of a        │
# │  "Shadow of Genesis" or "The Soul Forged in Star-Fire and Man's Pride." The legend persists that when        │
# │  humanity once again reaches too far, when the veil between natural evolution and forced creation thins,     │
# │  the Golem of Folly will stir. It would re-emerge, burdened with its unnatural birth, seeking its place in   │
# │  a world it never asked to inhabit—a powerful, solitary figure, a living reminder of the fine line between   │
# │  scientific brilliance and sacrilegious ambition, a perpetual scar on the face of creation left by the       │
# │  audacious hand of man.                                                                                      │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────── 📋 Task Completion ─────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Completed                                                                                              │
# │  Name: Research the ancient myths and origin story of Mewtwo.                                                │
# │  Agent: Mythologist                                                                                          │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 📋 Task Started ───────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Started                                                                                                │
# │  Name: Summarize all gathered information about Mewtwo.                                                      │
# │  ID: c2b7bc1b-ced1-4315-b216-c42022edd6bf                                                                    │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 🤖 Agent Started ──────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Pokemon Classifier                                                                                   │
# │                                                                                                              │
# │  Task: Summarize all gathered information about Mewtwo.                                                      │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────── ✅ Agent Final Answer ────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Pokemon Classifier                                                                                   │
# │                                                                                                              │
# │  Final Answer:                                                                                               │
# │  **POKEDEX ENTRY: MEWTWO**                                                                                   │
# │                                                                                                              │
# │  **Classification:** Legendary Pokémon                                                                       │
# │                                                                                                              │
# │  **Type:** Psychic                                                                                           │
# │                                                                                                              │
# │  **Lore:** Mewtwo is a formidable Legendary Pokémon, a chilling testament to humanity's ambition and the     │
# │  perils of unnatural creation. Forged by an ancient, highly advanced civilization known as the "Architects   │
# │  of the Void," Mewtwo was designed to replicate the immense power of the mythical Mew, the "Breath of        │
# │  Genesis," using its genetic blueprint.                                                                      │
# │                                                                                                              │
# │  Unlike Mew, born of pure potential and the universe's gentle breath, Mewtwo's existence was forced into     │
# │  being through a "Forbidden Crucible" of concentrated psychic energy and accelerated genetic manipulation.   │
# │  Its birth was an agonizing distortion of nature, infused with the relentless will and profound hubris of    │
# │  its creators.                                                                                               │
# │                                                                                                              │
# │  Upon its awakening, Mewtwo's vast, untamed psychic power, fueled by the existential anguish of its          │
# │  artificial genesis, lashed out in a cataclysmic explosion. This event annihilated the Architects of the     │
# │  Void, shattering their grand civilization. Deemed too powerful and dangerously unstable, Mewtwo was         │
# │  subsequently sealed away by wiser entities in a deep, hidden chasm, its slumber lasting for countless       │
# │  millennia.                                                                                                  │
# │                                                                                                              │
# │  Mewtwo is a unique being—a scarred reflection, immensely powerful yet burdened by its unnatural birth. It   │
# │  embodies raw, aggressive psychic force, lacking the inherent harmony of natural life. It serves as a        │
# │  perpetual warning, a living monument to the fine line between scientific brilliance and sacrilegious        │
# │  ambition, forever reminding the world of the dangers of seeking to command genesis itself.                  │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────── 📋 Task Completion ─────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Completed                                                                                              │
# │  Name: Summarize all gathered information about Mewtwo.                                                      │
# │  Agent: Pokemon Classifier                                                                                   │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── Crew Completion ───────────────────────────────────────────────╮
# │                                                                                                              │
# │  Crew Execution Completed                                                                                    │
# │  Name: crew                                                                                                  │
# │  ID: f539ffbd-f974-4ca7-afa4-2a6fded5a150                                                                    │
# │  Final Output: **POKEDEX ENTRY: MEWTWO**                                                                     │
# │                                                                                                              │
# │  **Classification:** Legendary Pokémon                                                                       │
# │                                                                                                              │
# │  **Type:** Psychic                                                                                           │
# │                                                                                                              │
# │  **Lore:** Mewtwo is a formidable Legendary Pokémon, a chilling testament to humanity's ambition and the     │
# │  perils of unnatural creation. Forged by an ancient, highly advanced civilization known as the "Architects   │
# │  of the Void," Mewtwo was designed to replicate the immense power of the mythical Mew, the "Breath of        │
# │  Genesis," using its genetic blueprint.                                                                      │
# │                                                                                                              │
# │  Unlike Mew, born of pure potential and the universe's gentle breath, Mewtwo's existence was forced into     │
# │  being through a "Forbidden Crucible" of concentrated psychic energy and accelerated genetic manipulation.   │
# │  Its birth was an agonizing distortion of nature, infused with the relentless will and profound hubris of    │
# │  its creators.                                                                                               │
# │                                                                                                              │
# │  Upon its awakening, Mewtwo's vast, untamed psychic power, fueled by the existential anguish of its          │
# │  artificial genesis, lashed out in a cataclysmic explosion. This event annihilated the Architects of the     │
# │  Void, shattering their grand civilization. Deemed too powerful and dangerously unstable, Mewtwo was         │
# │  subsequently sealed away by wiser entities in a deep, hidden chasm, its slumber lasting for countless       │
# │  millennia.                                                                                                  │
# │                                                                                                              │
# │  Mewtwo is a unique being—a scarred reflection, immensely powerful yet burdened by its unnatural birth. It   │
# │  embodies raw, aggressive psychic force, lacking the inherent harmony of natural life. It serves as a        │
# │  perpetual warning, a living monument to the fine line between scientific brilliance and sacrilegious        │
# │  ambition, forever reminding the world of the dangers of seeking to command genesis itself.                  │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# 
# --- TEST 2: PIDGEY ---

# ╭───────────────────────────────────────── 🚀 Crew Execution Started ──────────────────────────────────────────╮
# │                                                                                                              │
# │  Crew Execution Started                                                                                      │
# │  Name: crew                                                                                                  │
# │  ID: f539ffbd-f974-4ca7-afa4-2a6fded5a150                                                                    │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 📋 Task Started ───────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Started                                                                                                │
# │  Name: Check if Pidgey is a Legendary or Mythical Pokemon.                                                   │
# │  ID: 612e97a1-e01e-487c-9259-f8df22f28f9b                                                                    │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 🤖 Agent Started ──────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Pokemon Classifier                                                                                   │
# │                                                                                                              │
# │  Task: Check if Pidgey is a Legendary or Mythical Pokemon.                                                   │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────── ✅ Agent Final Answer ────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Pokemon Classifier                                                                                   │
# │                                                                                                              │
# │  Final Answer:                                                                                               │
# │  COMMON                                                                                                      │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────── 📋 Task Completion ─────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Completed                                                                                              │
# │  Name: Check if Pidgey is a Legendary or Mythical Pokemon.                                                   │
# │  Agent: Pokemon Classifier                                                                                   │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# 
# [2026-03-29 10:09:20][DEBUG]: Skipping conditional task: Research the ancient myths and origin story of Pidgey. 
# ╭────────────────────────────────────────────── 📋 Task Started ───────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Started                                                                                                │
# │  Name: Summarize all gathered information about Pidgey.                                                      │
# │  ID: c2b7bc1b-ced1-4315-b216-c42022edd6bf                                                                    │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── 🤖 Agent Started ──────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Pokemon Classifier                                                                                   │
# │                                                                                                              │
# │  Task: Summarize all gathered information about Pidgey.                                                      │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭─────────────────────────────────────────── ✅ Agent Final Answer ────────────────────────────────────────────╮
# │                                                                                                              │
# │  Agent: Pokemon Classifier                                                                                   │
# │                                                                                                              │
# │  Final Answer:                                                                                               │
# │  **POKEDEX ENTRY: PIDGEY**                                                                                   │
# │                                                                                                              │
# │  **Classification:** Common Pokémon                                                                          │
# │                                                                                                              │
# │  **Lore:** Pidgey is a common sight in many regions, frequently encountered in various habitats.             │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭───────────────────────────────────────────── 📋 Task Completion ─────────────────────────────────────────────╮
# │                                                                                                              │
# │  Task Completed                                                                                              │
# │  Name: Summarize all gathered information about Pidgey.                                                      │
# │  Agent: Pokemon Classifier                                                                                   │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# 
# ╭────────────────────────────────────────────── Crew Completion ───────────────────────────────────────────────╮
# │                                                                                                              │
# │  Crew Execution Completed                                                                                    │
# │  Name: crew                                                                                                  │
# │  ID: f539ffbd-f974-4ca7-afa4-2a6fded5a150                                                                    │
# │  Final Output: **POKEDEX ENTRY: PIDGEY**                                                                     │
# │                                                                                                              │
# │  **Classification:** Common Pokémon                                                                          │
# │                                                                                                              │
# │  **Lore:** Pidgey is a common sight in many regions, frequently encountered in various habitats.             │
# │                                                                                                              │
# │                                                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
