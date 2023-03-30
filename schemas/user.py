from pydantic import BaseModel


class User(BaseModel):
    username: str = "platzi"
    password: str = "platzi"