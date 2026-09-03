#Create a FastAPI endpoint that validates a bearer token from the Authorization header.

from fastapi import FastAPI, Security, Header, HTTPException

app = FastAPI()

async def verify_token(x_token: str = Header(None)):
    if x_token != "secret-token":
        raise HTTPException(status_code=403, detail="Invalid token")
    return x_token

@app.get("/secure")
async def secure_endpoint(token: str = Security(verify_token)):
    return {"token": token}