#Create a FastAPI endpoint that validates request body using a Pydantic model
#with nested fields: a category with name and id.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Category(BaseModel):
    name: str
    id: int

class Item(BaseModel):
    title: str
    category: Category

@app.post("/item")
async def create_item(item: Item):
    return {"title": item.title, "category_name": item.category.name}