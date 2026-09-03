#Create a FastAPI endpoint that reads and returns a file from disk
#using FileResponse for file download simulation.

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/file")
async def get_file():
    return FileResponse(path="README.md", filename="README.md")