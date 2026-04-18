from fastapi import FastAPI
import json
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float

def read_data():
    with open("data.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/items")
def get_items():
    data = read_data()
    return data

@app.post("/items")
def create_item(item: Item):
    data = read_data()  
    new_id = len(data) + 1

    # 🔥 новый объект с ID
    new_item = {
        "id": new_id,
        "name": item.name,
        "price": item.price
    }

    # добавляем
    data.append(new_item)

    # сохраняем
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    return new_item

@app.delete("/items/{id}")
def delete_item(id: int):
    data = read_data()

    # удаляем по id
    data = [item for item in data if item["id"] != id]

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    return {"status": "deleted", "id": id}
    
@app.put("/items/{id}")
def update_item(id: int, item: Item):
    data = read_data()

    found = False

    for i in range(len(data)):
        if data[i]["id"] == id:
            data[i]["name"] = item.name
            data[i]["price"] = item.price
            found = True
            break

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    if not found:
        return {"error": "item not found"}

    return {"status": "updated", "id": id}

@app.delete("/del")
def delete_all():
    data = []

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    return {"status": "deleted"}

@app.get("/item/{id}")
def get_id(id: int):
    data = read_data()
    for item in data:
        if item["id"] == id:
            return item