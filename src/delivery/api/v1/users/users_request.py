from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    id: str
    name: str
    age: int


class UserUpdateRequest(BaseModel):
    name: str
    age: int
