"""
main.py — FastAPI entry point for AI Slides Generator

Initializes the app, sets CORS policy, includes route handlers,
and runs the backend server on localhost:8000.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import router
import uvicorn

app = FastAPI()

# Allow cross-origin requests (Streamlit frontend uses this)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# Register API endpoints from the router
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Slide Generator API"}

# Run the server (only if this file is executed directly)
if __name__ == "__main__":
    uvicorn.run("src.app.main:app", host = "127.0.0.1", port = 8000, reload = True)
