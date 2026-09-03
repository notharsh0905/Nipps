#Create a FastAPI endpoint that uses path parameters and multiple query parameters
#with default values: GET /search?q=python&limit=10&page=1

from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
async def search(q: str = "", limit: int = 10, page: int = 1):
    return {"query": q, "limit": limit, "page": page}