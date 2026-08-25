#Create a FastAPI endpoint that handles HTTP method restrictions (GET, POST, PUT, DELETE) and returns the method used.

from fastapi import FastAPI

app = FastAPI()

@app.api_route("/method", methods=["GET", "POST", "PUT", "DELETE"])
async def get_method(method: str = None):
    return {"method": method}