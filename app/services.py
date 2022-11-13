import os
from uuid import UUID

import sqlalchemy as sa
from fastapi_login import LoginManager

from .constants import ROLE_ADMIN
from .database import db
from .hashing import Hasher
from .models import Product, User
from .schemas import (
    ProductCreateSchema,
    ProductOutSchema,
    ProductUpdateSchema,
    UserCreateSchema,
    UserOutSchema,
    UserUpdateSchema,
)

SECRET = os.getenv("SECRET_KEY")
manager = LoginManager(SECRET, token_url="/auth/token")


class UserService:
    @classmethod
    def get_user_object_as_schema(self, user: User):
        return UserOutSchema(
            id=user.id,
            username=user.username,
            name=user.name,
            role=user.role,
            is_active=user.is_active,
        )

    @classmethod
    def get_user_by_username(self, username: str):
        return db.query(User).filter(User.username == username).first()

    @classmethod
    def get_user_by_id(self, user_id: UUID):
        return db.query(User).filter(User.id == user_id).first()

    @classmethod
    def create_user(self, user: UserCreateSchema):
        db_user = User(
            username=user.username,
            password=Hasher.get_password_hash(user.password),
            name=user.name,
            role=ROLE_ADMIN,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    @classmethod
    def update_user(self, db_user: User, user: UserUpdateSchema):
        update_data = user.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_user, key, value)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user


@manager.user_loader()
def load_user(username: str):
    user = UserService.get_user_by_username(username)
    return user


class ProductService:
    @classmethod
    def get_user_object_as_schema(self, user: User):
        return ProductOutSchema(
            id=user.id,
            username=user.username,
            name=user.name,
            role=user.role,
            is_active=user.is_active,
        )

    @classmethod
    def get_product_by_name(self, name: str):
        return (
            db.query(Product)
            .filter(sa.func.lower(Product.name).contains(name.lower(), autoescape=True))
            .first()
        )

    @classmethod
    def get_product_by_id(self, product_id: UUID, is_anonymous: bool):
        product = db.query(Product).filter(Product.id == product_id).first()

        if is_anonymous:
            # TODO: REGISTER QUERY
            pass

        return product

    @classmethod
    def create_product(self, product: ProductCreateSchema):
        db_product = Product(
            name=product.name, sku=product.sku, price=product.price, brand=product.brand
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return db_product

    @classmethod
    def update_product(self, db_product: Product, product: ProductUpdateSchema):
        update_data = product.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_product, key, value)

        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        # TODO: SEND NOTITICATION TO ADMINS

        return db_product
