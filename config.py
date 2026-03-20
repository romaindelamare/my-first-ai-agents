import os
from langchain_openai import ChatOpenAI
from openai import OpenAI
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

USE_GEMINI = True # True for Gemini, False for Ollama
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GEMINI_MODEL = "gemini-2.5-flash"
OLLAMA_KEY = "ollama"
OLLAMA_MODEL = "qwen3.5:2b"
OLLAMA_URL = "http://localhost:11434"

if USE_GEMINI:
    print("### Using Gemini API ###")
    crew_llm = LLM(
        model=GEMINI_MODEL,
        base_url=GEMINI_URL 
    )
    # For script day 3 to 5
    llm = ChatOpenAI(
        api_key=GEMINI_API_KEY,
        base_url=GEMINI_URL,
        model=GEMINI_MODEL
    )
    # For script day 1 & 2
    client = OpenAI(
        api_key=GEMINI_API_KEY,
        base_url=GEMINI_URL
    )
    model = GEMINI_MODEL
else:
    print("### Using Ollama ###")
    crew_llm = LLM(
        model=f"ollama/{OLLAMA_MODEL}",
        base_url=OLLAMA_URL 
    )
    # For script day 3 to 5
    llm = ChatOpenAI(
        api_key=OLLAMA_KEY,
        base_url=f"{OLLAMA_URL}/v1",
        model=OLLAMA_MODEL
    )
    # For script day 1 & 2
    client = OpenAI(
        base_url=f"{OLLAMA_URL}/v1",
        api_key=OLLAMA_KEY 
    )
    model = OLLAMA_MODEL
