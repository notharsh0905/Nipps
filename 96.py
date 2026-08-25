#Create a FastAPI endpoint that validates an email format using Pydantic and returns a confirmation.

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Email(BaseModel):
    email: EmailStr

@app.post("/validate-email")
async def validate_email(data: Email):
    return {"valid": True, "email": data.email}