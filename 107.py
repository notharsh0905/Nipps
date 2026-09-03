#Create a FastAPI app with middleware that logs every request's
#method, path, and query parameters.

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time

app = FastAPI()

@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start
    print(f"{request.method} {request.url.path} - {process_time:.4f}s")
    return response

@app.get("/")
async def root():
    return {"message": "Hello with middleware"}