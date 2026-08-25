#Create a FastAPI route that accepts multiple query parameters using a list (e.g., tags).
#Example: GET /items?tags=python&tags=fastapi -> {"tags": ["python", "fastapi"]}

from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
async def read_items(tags: list[str] = []):
    return {"tags": tags}