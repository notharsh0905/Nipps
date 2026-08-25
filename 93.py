#Create a FastAPI endpoint that returns a specific HTTP status code (201 Created) along with a JSON response.
#Useful for creating resources.

from fastapi import FastAPI, status

app = FastAPI()

@app.post("/item", status_code=status.HTTP_201_CREATED)
async def create_item():
    return {"item": "Created successfully"}