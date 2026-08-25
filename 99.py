#Create a FastAPI startup event that initializes a database connection or cache when the app starts.

from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup():
    print("FastAPI app starting up...")

@app.on_event("shutdown")
async def shutdown():
    print("FastAPI app shutting down...")