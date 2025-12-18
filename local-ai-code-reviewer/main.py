from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import requests


client = OpenAI(
    base_url="http://localhost:11434/v1",  # Ollama local endpoint
    api_key="ollama"  # Dummy key - Ollama doesn't require one
)

try:
    requests.get("http://localhost:11434")
except requests.ConnectionError:
    raise RuntimeError("Ollama is not running. Start it with 'ollama serve'")


class CodeReviewResponse(BaseModel):
    review: str


# initialize app instance
app = FastAPI(
    title="Local AI-Powered Code Review Tool",
    description="An API that reviews code snippets using Ollama (fully local and private)."
)

# get endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Local AI Code Reviewer! Use POST /review to submit code."}
