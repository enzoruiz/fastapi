from pydantic import BaseModel
from uuid import UUID


class UserCreateSchema(BaseModel):
    username: str
    password: str
    name: str

    class Config:
        orm_mode = True


class UserOutSchema(BaseModel):
    id: UUID
    username: str
    name: str
    role: str

    class Config:
        orm_mode = True


class ProductSchema(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    brand: str

    class Config:
        orm_mode = True
