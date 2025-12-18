# Local AI-Powered Code Review Tool

FastAPI service that uses Ollama to review code snippets locally.

Testing:

- Run the app: uvicorn main:app --reload
- Open browser to http://127.0.0.1:8000/ → Should see JSON: {"message": "Welcome to the Local AI Code 
Reviewer! Use POST /review to submit code."}
- Check docs: http://127.0.0.1:8000/docs → Swagger UI loads with the app title/description and a GET / endpoint.
