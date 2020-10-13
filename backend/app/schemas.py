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


class Order(pydantic.BaseModel):
    class Config:
        orm_mode = True

    id: str
    user: str
    item: str
    is_active: bool
    created_at: datetime.datetime


class OrderCreate(pydantic.BaseModel):
    user_id: str
    item_id: int
