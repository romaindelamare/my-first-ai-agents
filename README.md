# 🚀 My First AI Agents (30-Day Challenge)

This repository documents a 30-day journey from basic LLM scripts to advanced multi-agent systems. It explores the transition from procedural "if/else" logic to **Agentic Workflows** using **LangGraph** and **CrewAI**.

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
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install langchain-openai langchain-google-genai langgraph crewai "crewai[tools]" litellm python-dotenv google-generativeai ollama
```

## ⚙️ Configuration Strategy

The project uses a central `config.py` to decouple the application logic from the LLM provider (Strategy Pattern). This allows for seamless switching between local and cloud models.

- **Gemini Mode**: Set `USE_GEMINI = True` (Uses Google Gemini 2.5 Flash).
- **Ollama Mode**: Set `USE_GEMINI = False` (Uses local Qwen 3.5 via Ollama).

## 📂 Learning Roadmap

| Day | Topic | Script | Key Concept |
| :--- | :--- | :--- | :--- |
| **1-2** | **Basic LLM & Logic** | `day1_basic.py`, `day2_tools.py` | Manual loops and basic function calling. |
| **3-5** | **State Machines** | `day3_graph.py`, `day4_agent.py`, `day5_memory.py` | Building graphs with **LangGraph** and maintaining state. |
| **6-7** | **Multi-Agent Crews** | `day6_crew.py`, `day7_crew.py` | Collaborative AI using **CrewAI** and sequential processes. |
| **8-9** | **Tools & Search** | `day8_search.py`, `day9_custom_tool.py` | Integrating Web Search (Serper) and custom Python `@tool` decorators. |
| **10** | **Human-in-the-Loop** | `day10_hitl.py` | Adding human approval gates (`human_input=True`) to agent tasks. |