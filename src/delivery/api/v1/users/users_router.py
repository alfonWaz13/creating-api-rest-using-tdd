from fastapi import APIRouter, Depends
from http.client import CREATED

from src.delivery.api.v1.users.users_request import CreateUserRequest
from src.domain.user import User
from src.use_cases.commands.create_user_command import (
    CreateUserCommandHandler,
    CreateUserCommand,
)

users_router = APIRouter()


def _get_create_user_command_handler() -> CreateUserCommandHandler:
    return CreateUserCommandHandler()


@users_router.post("/", status_code=CREATED)
def create_user(
    user_request: CreateUserRequest,
    handler: CreateUserCommandHandler = Depends(_get_create_user_command_handler),
) -> None:
    user = User(**user_request.model_dump())
    command = CreateUserCommand(user)
    handler.execute(command)
