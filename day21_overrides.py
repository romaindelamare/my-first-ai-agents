from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI
import config

# 1. Define a "Creative" Model for the Writer
creative_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,
    top_p=0.95
)

# 2. THE AGENTS
researcher = Agent(
    role="Data Gatherer",
    goal="Collect raw numbers for {pokemon}.",
    backstory="You are a machine. You only care about integers and types.",
    llm=config.crew_llm, # Uses the "Fast/Cheap" model
    verbose=True
)

writer = Agent(
    role="Creative Content Creator",
    goal="Write an engaging, poetic description of {pokemon}.",
    backstory="You are a master wordsmith with a flair for the dramatic.",
    llm=creative_llm, # OVERRIDE: Uses the "Smart/Expensive" model
    verbose=True
)

# 3. THE TASKS
task1 = Task(description="Get base stats for {pokemon}.", expected_output="Numeric stats.", agent=researcher)
task2 = Task(description="Write a 1-page poetic essay.", expected_output="A poetic essay.", agent=writer)

# 4. THE CREW
optimized_crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True
)

print("### Running Day 21: Model Overrides")
optimized_crew.kickoff(inputs={'pokemon': 'Rayquaza'})

### LOG RESULT with Gemini ###

# Beyond the reach of clouds, where air thins to a whisper and the sun is a brutal, unblinking eye,      │
# there dwells a sovereign of solitude. Not born of earth, nor sea, but forged in the fiery breath of    │
# distant stars, its kingdom is the stratospheric silence, its throne the boundless, inky black. This    │
# is the Emerald Zenith, the Sky's Ascendant, Rayquaza.                                                  │
#                                                                                                        │
# Imagine, if you dare, the serpentine majesty. A living aurora, shimmering with scales of deepest jade  │
# and obsidian, etched with luminous gold that pulses like captured starlight. Its form, a cosmic        │
# ribbon, weaves through the void, each undulation a ripple in the fabric of space itself. It is the     │
# breath of the heavens made manifest, an ancient dragon whose roar is the echo of collapsing suns,      │
# whose gaze holds the wisdom of epochs.                                                                 │
#                                                                                                        │
# Within its colossal frame beats a heart of pure cosmic energy, a life-force of **105** measures,       │
# robust and enduring, steadfast against the gnawing vacuum, a testament to its singular existence. And  │
# from this core springs forth a power both raw and refined. A flick of its mighty tail can cleave the   │
# very air, a physical strike imbued with **150** points of unbridled force, capable of shattering       │
# mountains or parting storms. Yet, its intellect is equally potent; from its luminous jaws, a torrent   │
# of astral fire, a beam of pure thought given form, its special fury, a twin **150**, rivaling its      │
# brute strength, an annihilation whispered into being.                                                  │
#                                                                                                        │
# Not invulnerable, for even gods know their limits, yet encased in scales of formidable resilience, a   │
# shell of defense, ninety strong. Against the esoteric energies that may seek to pierce its aura, a     │
# guardian’s will provides a second, equally robust, ninety-fold shield, deflecting the arcane. Across   │
# the celestial tapestry it streaks, a vibrant emerald comet, swifter than the eye can follow, a blur    │
# of ancient power, ninety-five measures of grace and acceleration, leaving behind trails of shimmering  │
# stardust.                                                                                              │
#                                                                                                        │
# It is the mediating force, the still point between chaos and order, its very presence a balm to the    │
# warring titans below. When the earth rumbles with primal fury and the seas rise in vengeful deluge,    │
# it descends, a verdant meteor, not to destroy, but to restore balance. Its lonely vigil in the ozone   │
# layer is a ceaseless dance, a cosmic ballet of power and restraint. Rayquaza, the sky serpent, the     │
# celestial guardian, forever soaring, a silent, breathtaking testament to the awe-inspiring, dramatic   │
# might of the heavens.