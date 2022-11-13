from typing import Union

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from fastapi import FastAPI
from pydantic import BaseModel

# from . import crud, models, schemas
from .models import Base, User
from .schemas import UserCreateSchema, UserOutSchema
from .services import UserService
from .database import SessionLocal, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/", response_model=UserOutSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = UserService.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return UserService.create_user(db=db, user=user)


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
