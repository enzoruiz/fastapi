import datetime
import uuid

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "myuser"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True, primary_key=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)
    role = Column(String)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )


class Product(Base):
    __tablename__ = "product"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True, primary_key=True)
    name = Column(String(90))
    sku = Column(String(25))
    price = Column(Float)
    brand = Column(String(25))
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
