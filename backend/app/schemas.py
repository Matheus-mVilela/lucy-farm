import typing
import datetime

import pydantic


class User(pydantic.BaseModel):
    class Config:
        orm_mode = True

    username: str
    email: pydantic.EmailStr


class UserCreate(User):
    password: str


class Item(pydantic.BaseModel):
    name: str
    price: float
    measure: str


class ItemDetail(Item):
    order_id: str


class OrderItemDetail(pydantic.BaseModel):
    class Config:
        orm_mode = True

    id: str
    item_id: int
    price: float
    discount: float
    quantity: int


class Order(pydantic.BaseModel):
    class Config:
        orm_mode = True

    id: str
    user_id: str
    items: typing.List[OrderItemDetail]
    is_active: bool
    created_at: datetime.datetime


class OrderCreate(pydantic.BaseModel):
    user_id: str
    items_id: typing.List[int]
    price: float
    discount: float
    quantity: int
