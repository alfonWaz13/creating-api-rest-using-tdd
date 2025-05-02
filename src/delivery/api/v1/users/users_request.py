from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    name: str
    age: int
