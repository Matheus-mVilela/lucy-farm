import datetime
import uuid

import sqlalchemy
import sqlalchemy.orm

from .database import Base


class User(Base):
    # TODO: This class will use APIKey
    __tablename__ = 'users'

    id = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
        unique=True,
        index=True,
        default=lambda: str(uuid.uuid4()),
    )
    username = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    hashed_password = sqlalchemy.Column(
        sqlalchemy.String, nullable=True, default=None
    )


class Item(Base):
    __tablename__ = 'items'

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, unique=True, index=True
    )
    name = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Float)
    measure = sqlalchemy.Column(sqlalchemy.String)


class Order(Base):
    __tablename__ = 'orders'

    id = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
        unique=True,
        index=True,
        default=lambda: str(uuid.uuid4()),
    )
    user = sqlalchemy.Column(
        sqlalchemy.String, sqlalchemy.ForeignKey('users.id')
    )
    item = sqlalchemy.Column(
        sqlalchemy.String, sqlalchemy.ForeignKey('items.id')
    )
    is_active = sqlalchemy.Column(sqlalchemy.Boolean)
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.utcnow
    )
