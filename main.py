from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_world():
    return {"message": "hello world"}


@app.get("/hello/")
def hello(name: str = "world"):
    return {"hello": f"hello {name}"}


@app.post("/users/")
def create_user(user: CreateUser):
    return {"email": user.email}


@app.get("/item/")
def items():
    return [{"items1": "11111"}, {"items2": "222222"}]


@app.get("/item/{item_id}/")
def get_item_by_id(item_id: int):
    return {"item": {"id": item_id}}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
