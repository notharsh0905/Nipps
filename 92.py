#Create a FastAPI endpoint that accepts a JSON request body using a Pydantic model for a person (name and age).
#Example POST with {"name": "Bob", "age": 30} -> {"person": {"name": "Bob", "age": 30}}

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int

@app.post("/person")
async def create_person(person: Person):
    return {"person": person.dict()}