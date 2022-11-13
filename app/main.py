from typing import Union

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi import FastAPI
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from uuid import UUID

from .schemas import UserCreateSchema, UserOutSchema, UserUpdateSchema, ProductCreateSchema, ProductOutSchema, ProductUpdateSchema
from .services import UserService, ProductService, manager, load_user
from .hashing import Hasher
from .constants import ROLE_ADMIN

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/auth/token')
def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password

    user = load_user(username)

    if not user:
        raise InvalidCredentialsException
    elif not Hasher.verify_password(password, user.password):
        raise InvalidCredentialsException
    
    access_token = manager.create_access_token(
        data=dict(sub=username, username=username)
    )

    return {'access_token': access_token, 'token_type': 'bearer'}


@app.post("/users/", response_model=UserOutSchema)
def create_user(user: UserCreateSchema, logged_user=Depends(manager)):
    if logged_user.role == ROLE_ADMIN:
        db_user = UserService.get_user_by_username(username=user.username)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return UserService.create_user(user=user)
    else:
        raise HTTPException(status_code=401, detail="Not authorized to create users")


@app.post("/users/update/", response_model=UserOutSchema)
def update_user(user_id: UUID, user: UserUpdateSchema, logged_user=Depends(manager)):
    if logged_user.role == ROLE_ADMIN:
        db_user = UserService.get_user_by_id(user_id=user_id)
        if not db_user:
            raise HTTPException(status_code=400, detail="Invalid User")

        return UserService.update_user(db_user, user)
    else:
        raise HTTPException(status_code=401, detail="Not authorized to update users")


@app.post("/products/", response_model=ProductOutSchema)
def create_product(product: ProductCreateSchema, logged_user=Depends(manager)):
    if logged_user.role == ROLE_ADMIN:
        db_product = ProductService.get_product_by_name(name=product.name)
        if db_product:
            raise HTTPException(status_code=400, detail="Product already registered")
        return ProductService.create_product(product=product)
    else:
        raise HTTPException(status_code=401, detail="Not authorized to create products")


@app.post("/products/update/", response_model=ProductOutSchema)
def update_product(product_id: UUID, product: ProductUpdateSchema, logged_user=Depends(manager)):
    if logged_user.role == ROLE_ADMIN:
        db_product = ProductService.get_product_by_id(product_id=product_id)
        if not db_product:
            raise HTTPException(status_code=400, detail="Invalid User")

        return ProductService.update_product(db_product, product)
    else:
        raise HTTPException(status_code=401, detail="Not authorized to update products")


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
