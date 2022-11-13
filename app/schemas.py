from pydantic import BaseModel
from uuid import UUID
from typing import Optional


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
    is_active: bool

    class Config:
        orm_mode = True


class UserUpdateSchema(BaseModel):
    username: Optional[str]
    name: Optional[str]
    is_active: Optional[bool]

    class Config:
        orm_mode = True


class ProductCreateSchema(BaseModel):
    name: str
    sku: str
    price: float
    brand: str

    class Config:
        orm_mode = True


class ProductOutSchema(BaseModel):
    id: UUID
    name: str
    sku: str
    price: float
    brand: str
    is_active: bool

    class Config:
        orm_mode = True


class ProductUpdateSchema(BaseModel):
    name: Optional[str]
    sku: Optional[str]
    price: Optional[float]
    brand: Optional[str]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
