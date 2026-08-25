#Create a minimal FastAPI application that returns "Hello, World!" at the root endpoint.
#Run with: uvicorn filename:app

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}