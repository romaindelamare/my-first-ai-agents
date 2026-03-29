from crewai import Agent, Task, Crew
import config

analyzer = Agent(
    role="Cost Analyst",
    goal="Summarize the battle stats for {pokemon}.",
    backstory="You are efficient and use as few words as possible.",
    llm=config.crew_llm
)

task = Task(
    description="Analyze {pokemon} and its main weakness.",
    expected_output="A single sentence summary.",
    agent=analyzer
)

crew = Crew(
    agents=[analyzer],
    tasks=[task],
    verbose=False
)

result = crew.kickoff(inputs={'pokemon': 'Charizard'})

metrics = result.token_usage

# Current Gemini 2.5 Flash Rates (Standard Tier)
# $0.10 per 1M Input Tokens
# $0.40 per 1M Output Tokens
INPUT_RATE_PER_TOKEN = 0.0000001
OUTPUT_RATE_PER_TOKEN = 0.0000004

prompt_tokens = metrics.prompt_tokens
completion_tokens = metrics.completion_tokens

# Calculate split costs
input_cost = prompt_tokens * INPUT_RATE_PER_TOKEN
output_cost = completion_tokens * OUTPUT_RATE_PER_TOKEN
total_cost = input_cost + output_cost

print("\n" + "="*30)
print("   GEMINI 2.5 FLASH BILLING")
print("="*30)
print(f"Prompt Cost:     ${input_cost:.6f}")
print(f"Completion Cost: ${output_cost:.6f}")
print("-"*30)
print(f"TOTAL TASK COST: ${total_cost:.6f}")
print("="*30)

### LOG RESULT with Gemini ###
# ==============================
#    GEMINI 2.5 FLASH BILLING
# ==============================
# Prompt Cost:     $0.000008
# Completion Cost: $0.000010
# ------------------------------
# TOTAL TASK COST: $0.000019
# ==============================