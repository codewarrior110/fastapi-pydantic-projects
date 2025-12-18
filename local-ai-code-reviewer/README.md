# Local AI-Powered Code Review Tool

FastAPI service that uses Ollama to review code snippets locally.

Testing (#Phase 1):

- Run the app: uvicorn main:app --reload
- Open browser to http://127.0.0.1:8000/ → Should see JSON: {"message": "Welcome to the Local AI Code 
Reviewer! Use POST /review to submit code."}
- Check docs: http://127.0.0.1:8000/docs → Swagger UI loads with the app title/description and a GET / endpoint.

Testing (#Phase 2):

- Ensure Ollama model is pulled: ollama pull deepseek-coder-v2
- Run Ollama: ollama serve
- Run app: uvicorn main:app --reload
- Browser: http://127.0.0.1:8000/docs → See new POST /review endpoint.

- Try it in Swagger: Input code like print("hello"), language python, model deepseek-coder-v2. Should    return a JSON review. If model missing, error in logs.
