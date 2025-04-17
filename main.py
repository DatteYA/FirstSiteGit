from typing import Annotated

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

from item_views import router as items_router
from users.views import router as user_router
from core.models import db_helper, Base
from apiv1 import router as router_v1
from core.config import settings


from contextlib import asynccontextmanager

import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    pass



app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(user_router)
app.include_router(router=router_v1, prefix=settings.apiv1_prefix)


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_world():
    return {"message": "Hello world"}


@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


@app.post("/hello")
def helloUser(name: str = "PIDARAS"):
    name = name.strip().title()
    return {"Bombardino": f"Hello {name}"}


@app.get("/newuser/")
def create_user(user: CreateUser):
    return {"User": f"create with {user.email}"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
