import datetime
import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

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


class ProductLog(Base):
    __tablename__ = "product_log"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True, primary_key=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))
    ip_address = Column(String, default=None)

    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
