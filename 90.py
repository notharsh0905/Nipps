#Create a FastAPI endpoint that accepts a path parameter user_id and returns a greeting.
#Example: GET /users/123 -> {"user_id": 123, "message": "User 123"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id, "message": f"User {user_id}"}