#Create a FastAPI endpoint that accepts a path parameter and an optional query parameter.
#GET /books/{book_id}?format=json -> {"book_id": book_id, "format": format}

from fastapi import FastAPI

app = FastAPI()

@app.get("/books/{book_id}")
async def read_book(book_id: int, format: str = None):
    result = {"book_id": book_id}
    if format:
        result["format"] = format
    return result