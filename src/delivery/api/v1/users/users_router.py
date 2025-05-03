from fastapi import APIRouter, Depends
from http.client import CREATED

from src.delivery.api.v1.users.users_request import CreateUserRequest
from src.domain.user import User
from src.infraestructure.in_memory.users_repository import InMemoryUsersRepository
from src.use_cases.commands.create_user_command import (
    CreateUserCommandHandler,
    CreateUserCommand,
)

users_router = APIRouter()
users_repository = InMemoryUsersRepository()


def _get_create_user_command_handler() -> CreateUserCommandHandler:
    return CreateUserCommandHandler(users_repository)


@users_router.post("/", status_code=CREATED)
def create_user(
    user_request: CreateUserRequest,
    handler: CreateUserCommandHandler = Depends(_get_create_user_command_handler),
) -> None:
    user = User(**user_request.model_dump())
    command = CreateUserCommand(user)
    handler.execute(command)
