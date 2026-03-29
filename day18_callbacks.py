import json
import os
import logging
from crewai import Agent, Task, Crew
import config

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def save_to_history(output):
    """
    Day 18 Callback: Persists task results to a structured JSON file.
    """
    directory = "history"
    filename = os.path.join(directory, "task_log.json")

    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"Created directory: {directory}")

    new_entry = {
        "description": output.description,
        "summary": output.raw[:100] + "...", # Truncated for the log
        "full_result": output.raw,
        "timestamp": "2026-03-29"
    }

    history = []

    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                history = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            logging.warning(f"Malformed or missing {filename}. Starting new log.")
            history = []
        except Exception as e:
            logging.error(f"Unexpected error reading history: {e}")
            return

    history.append(new_entry)

    try:
        with open(filename, "w") as f:
            json.dump(history, f, indent=4)
        logging.info(f"Successfully saved results to {filename}")
    except IOError as e:
        logging.error(f"Disk error: Could not write to {filename}. {e}")

researcher = Agent(
    role="Pokemon Lore Analyst",
    goal="Extract the secret habitat of {pokemon}.",
    backstory="You are a specialist in geographical Pokemon data.",
    llm=config.crew_llm,
    verbose=True
)

habitat_task = Task(
    description="Research the most likely natural habitat for {pokemon}.",
    expected_output="A description of the environment and climate.",
    agent=researcher,
    callback=save_to_history # Hooked into our Day 18 function
)

habitat_crew = Crew(
    agents=[researcher],
    tasks=[habitat_task],
    verbose=True
)

if __name__ == "__main__":
    print("### Starting Day 18: Task Callbacks & Persistence")
    habitat_crew.kickoff(inputs={'pokemon': 'Gengar'})