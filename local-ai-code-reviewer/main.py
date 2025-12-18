from fastapi import FastAPI
from pydantic import BaseModel


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
