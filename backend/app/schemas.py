import pydantic


class User(pydantic.BaseModel):
    class Config:
        orm_mode = True

    username: str
    email: str


class UserCreate(User):
    password: str
