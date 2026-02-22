

from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello from Client B Python App",
        "client": "Client B",
        "environment": os.getenv("ENVIRONMENT", "dev")
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
