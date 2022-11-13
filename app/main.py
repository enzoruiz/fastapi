from uuid import UUID

from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

from fastapi import Depends, FastAPI, HTTPException

from .constants import ROLE_ADMIN
from .hashing import Hasher
from .schemas import (
    ProductCreateSchema,
    ProductOutSchema,
    ProductUpdateSchema,
    UserCreateSchema,
    UserOutSchema,
    UserUpdateSchema,
)
from .services import ProductService, UserService, load_user, manager

app = FastAPI()
depends = Depends()
manager_depends = Depends(manager)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/auth/token")
def login(data: OAuth2PasswordRequestForm = depends):
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

    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/", response_model=UserOutSchema)
def create_user(user: UserCreateSchema, logged_user=manager_depends):
    if logged_user.role == ROLE_ADMIN:
        db_user = UserService.get_user_by_username(username=user.username)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return UserService.create_user(user=user)
    else:
        raise HTTPException(status_code=401, detail="Not authorized to create users")


@app.post("/users/update/", response_model=UserOutSchema)
def update_user(user_id: UUID, user: UserUpdateSchema, logged_user=manager_depends):
    if logged_user.role == ROLE_ADMIN:
        db_user = UserService.get_user_by_id(user_id=user_id)
        if not db_user:
            raise HTTPException(status_code=400, detail="Invalid User")

        return UserService.update_user(db_user, user)
    else:
        raise HTTPException(status_code=401, detail="Not authorized to update users")


@app.post("/products/", response_model=ProductOutSchema)
def create_product(product: ProductCreateSchema, logged_user=manager_depends):
    if logged_user.role == ROLE_ADMIN:
        db_product = ProductService.get_product_by_name(name=product.name)
        if db_product:
            raise HTTPException(status_code=400, detail="Product already registered")
        return ProductService.create_product(product=product)
    else:
        raise HTTPException(status_code=401, detail="Not authorized to create products")


@app.get("/products/{product_id}", response_model=ProductOutSchema)
def get_product(product_id: UUID):
    db_product = ProductService.get_product_by_id(
        product_id=product_id, is_anonymous=True
    )
    if not db_product:
        raise HTTPException(status_code=404, detail="Product does not exist!")
    return db_product


@app.post("/products/update/", response_model=ProductOutSchema)
def update_product(
    product_id: UUID, product: ProductUpdateSchema, logged_user=manager_depends
):
    if logged_user.role == ROLE_ADMIN:
        db_product = ProductService.get_product_by_id(
            product_id=product_id, is_anonymous=False
        )
        if not db_product:
            raise HTTPException(status_code=400, detail="Invalid User")

        return ProductService.update_product(db_product, product)
    else:
        raise HTTPException(status_code=401, detail="Not authorized to update products")
