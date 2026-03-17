import os
from langchain_openai import ChatOpenAI
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Set this to True for Gemini, False for Ollama
USE_GEMINI = False
GEMINI_ENV_API_KEY = "GEMINI_API_KEY"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GEMINI_MODEL = "gemini-2.5-flash"
OLLAMA_KEY = "ollama"
OLLAMA_MODEL = "qwen3.5:2b"
OLLAMA_URL = "http://localhost:11434/v1"

if USE_GEMINI:
    llm = ChatOpenAI(
        api_key=os.getenv(GEMINI_ENV_API_KEY),
        base_url=GEMINI_URL,
        model=GEMINI_MODEL
    )
    # For script day 1 & 2
    client = OpenAI(
        api_key=os.getenv(GEMINI_ENV_API_KEY),
        base_url=GEMINI_URL
    )
    model = GEMINI_MODEL
else:
    llm = ChatOpenAI(
        api_key=OLLAMA_KEY,
        base_url=OLLAMA_URL,
        model=OLLAMA_MODEL
    )
    # For script day 1 & 2
    client = OpenAI(
        base_url=OLLAMA_URL,
        api_key=OLLAMA_KEY 
    )
    model = OLLAMA_MODEL
