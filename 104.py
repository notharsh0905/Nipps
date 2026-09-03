#Create a FastAPI endpoint that demonstrates path operation decorators
#with different methods on the same path.

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.put("/items/{item_id}")
async def update_item(item_id: int, q: int = None):
    return {"item_id": item_id, "q": q}