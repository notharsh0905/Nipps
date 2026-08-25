#Create a FastAPI endpoint that accepts query parameters: name and age, and returns a personalized greeting.
#Example: GET /greet?name=Alice&age=25 -> {"message": "Hello Alice, you are 25 years old!"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
async def greet(name: str = "Anonymous", age: int = 0):
    return {"message": f"Hello {name}, you are {age} years old!"}