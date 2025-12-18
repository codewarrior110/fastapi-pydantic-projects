from fastapi import FastAPI

app = FastAPI(
    title="Local AI-Powered Code Review Tool",
    description="An API that reviews code snippets using Ollama (fully local and private)."
)

@app.get("/")
def home():
    return {"message": "Welcome to the Local AI Code Reviewer! Use POST /review to submit code."}
