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

    user: User
    item: Item
    is_active: bool
