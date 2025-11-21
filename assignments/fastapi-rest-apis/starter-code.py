from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


app = FastAPI(title="FastAPI Starter - APIs REST")

# In-memory "database"
db = [
    {"id": 1, "name": "Caneta", "description": "Caneta azul", "price": 1.5},
    {"id": 2, "name": "Caderno", "description": "Caderno A4", "price": 12.0},
]


@app.get("/items", response_model=List[Item])
def list_items():
    return db


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in db:
        if it["id"] == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item não encontrado")


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    for it in db:
        if it["id"] == item.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    db.append(item.dict())
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for i, it in enumerate(db):
        if it["id"] == item_id:
            db[i] = item.dict()
            return db[i]
    raise HTTPException(status_code=404, detail="Item não encontrado")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for i, it in enumerate(db):
        if it["id"] == item_id:
            db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Item não encontrado")


if __name__ == "__main__":
    # Executar diretamente com: python starter-code.py
    uvicorn.run(app, host="127.0.0.1", port=8000)
