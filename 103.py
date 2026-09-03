#Create a FastAPI endpoint that returns a JSONResponse with a custom status code
#and headers: Set a "X-Custom-Header" header.

from fastapi import FastAPI, Response, status

app = FastAPI()

@app.get("/custom-response")
async def custom_response():
    content = {"message": "This has a custom status and header"}
    return Response(content=content, status_code=status.HTTP_201_CREATED, headers={"X-Custom-Header": "custom-value"})