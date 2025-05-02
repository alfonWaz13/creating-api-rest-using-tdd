from fastapi import APIRouter
from http.client import CREATED

from src.delivery.api.v1.users.users_request import CreateUserRequest

users_router = APIRouter()


@users_router.post("/", status_code=CREATED)
def create_user(user_request: CreateUserRequest) -> None:
    pass
