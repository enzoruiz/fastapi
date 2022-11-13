from sqlalchemy.orm import Session

from .schemas import UserCreateSchema, ProductSchema
from .models import User, Product
from .hashing import Hasher


class UserService:
    @classmethod
    def get_user_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    @classmethod
    def create_user(self, db: Session, user: UserCreateSchema):
        db_user = User(
            username=user.username,
            password=Hasher.get_password_hash(user.password),
            name=user.name,
            role="admin"
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()





def create_user_item(db: Session, product: ProductSchema, user_id: int):
    db_item = Product(**product.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
