# 🚀 My First AI Agents

This repository documents a 24-step journey from basic LLM scripts to advanced multi-agent systems. It explores the transition from procedural "if/else" logic to **Agentic Workflows** using **LangGraph** and **CrewAI**.

## 🛠️ Prerequisites

1. **Python 3.10+**
2. **Ollama**: [Download here](https://ollama.com/)
   - Models used:
     ```bash
     ollama pull qwen3.5:2b
     ollama pull nomic-embed-text
     ```
3. **API Keys**: Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_google_key_here
   GOOGLE_API_KEY=your_google_key_here
   SERPER_API_KEY=your_serper_dev_key_here
   ```

## 📦 Installation

```bash
# Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate # Windows
# source venv/bin/activate  # Linux/Mac

# Install Core Frameworks
pip install crewai langgraph langchain-openai langchain-google-genai 

# Install Essential Tools & Providers
pip install "crewai[tools]" litellm python-dotenv google-generativeai ollama

# Install Local Database & Memory Support (Crucial for Day 11+)
pip install lancedb pyarrow
```

## ⚙️ Configuration Strategy

The project uses a central `config.py` to decouple the application logic from the LLM provider (Strategy Pattern). This allows for seamless switching between local and cloud models.

- **Gemini Mode**: Uses **Google Gemini 2.5 Flash** for high-speed, low-cost reasoning.
- **Ollama Mode**: Uses local **Qwen 3.5** via Ollama for privacy and offline development.

## 📂 Learning Roadmap

| Day | Topic | Script | Key Concept |
| :--- | :--- | :--- | :--- |
| **1-5** | **Foundations** | `day1.py` - `day5.py` | Basic LLM logic, LangGraph nodes, and State Management. |
| **6-10** | **Crews & Tools** | `day6.py` - `day10.py` | Collaborative Agents, Custom `@tool` decorators, and Serper Search. |
| **11-12** | **Memory & RAG** | `day11_mem.py`, `day12_rag.py` | Vector DBs (LanceDB) and grounding agents in `.txt` documentation. |
| **13-14** | **Execution Flow** | `day13_async.py`, `day14_json.py` | Async task execution and Structured JSON output via Pydantic. |
| **15-16** | **Optimization** | `day15_del.py`, `day16_train.py` | Agent delegation and using `crew.train()` for feedback loops. |
| **17** | **Usage Metrics** | `day17_metrics.py` | Tracking tokens (Prompt/Completion) and calculating real-world API costs. |
| **18** | **Event Callbacks** | `day18_callbacks.py` | Triggering Python functions (JSON logging) automatically on task completion. |
| **19** | **Conditional Tasks** | `day19_logic.py` | Branching logic: triggering specific tasks only if conditions are met. |
| **20** | **Strategic Planning** | `day20_planning.py` | Enabling the `planning=True` phase for step-by-step task architecture. |
| **21** | **Model Overrides** | `day21_overrides.py` | Mixing models (Flash vs. Pro) to optimize cost and creative quality. |
| **22** | **Forced Tool Use** | `day22_force.py` | Using "Amnesia" personas to ensure agents use tools instead of guessing. |
| **23** | **Self-Correction** | `day23_qa.py` | Implementing a Senior Auditor agent to review and reject Junior work. |
| **24** | **Hierarchical Crew** | `day24_manager.py` | Autonomous management using `Process.hierarchical` and a Manager LLM. |

## 🧪 Key Learnings

- **Model Tiering**: Using Gemini 2.5 Flash for 90% of tasks saves significant cost without sacrificing quality when paired with strong prompts.
- **Hierarchical vs Sequential**: Sequential is great for simple pipelines, but Hierarchical is necessary for complex projects requiring autonomous oversight.
- **The "Amnesia" Persona**: A powerful prompt engineering technique to force agents to rely on RAG/Tools rather than internal training data (hallucinations).