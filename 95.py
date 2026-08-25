#Create a FastAPI endpoint that reads a file from the local filesystem and returns its content as a downloadable response.
#Use: from fastapi.responses import FileResponse

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/download")
async def download():
    return FileResponse(path="README.md", filename="README.md", media_type="text/markdown")