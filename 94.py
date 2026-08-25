#Create a FastAPI endpoint that uses dependency injection to get a common header (e.g., Authorization) from requests.

from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

async def get_token_header(x_token: str = Header(None)):
    if x_token != "secret-token":
        raise HTTPException(status_code=403, detail="Invalid X-Token header")
    return x_token

@app.get("/protected")
async def protected(token: str = Depends(get_token_header)):
    return {"token": token, "message": "Access granted"}