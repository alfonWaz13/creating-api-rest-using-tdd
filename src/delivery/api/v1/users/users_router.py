from fastapi import APIRouter, Depends
from http.client import CREATED, OK, NO_CONTENT

from src.delivery.api.v1.users.users_request import CreateUserRequest, UserUpdateRequest
from src.delivery.api.v1.users.users_responses import UsersResponse, UserResponse
from src.domain.user import User
from src.infraestructure.in_memory.users_repository import InMemoryUsersRepository
from src.use_cases.commands.create_user_command import (
    CreateUserCommandHandler,
    CreateUserCommand,
)
from src.use_cases.commands.delete_user_command import (
    DeleteUserCommandHandler,
    DeleteUserCommand,
)
from src.use_cases.commands.update_user_command import (
    UpdateUserCommandHandler,
    UpdateUserCommand,
)
from src.use_cases.queries.find_all_users_query import FindAllUsersQueryHandler
from src.use_cases.queries.find_one_user_query import (
    FindOneUserQueryHandler,
    FindOneUserQuery,
)

users_router = APIRouter()
users_repository = InMemoryUsersRepository()


def _get_create_user_command_handler() -> CreateUserCommandHandler:
    return CreateUserCommandHandler(users_repository)


def _get_find_all_users_query_handler() -> FindAllUsersQueryHandler:
    return FindAllUsersQueryHandler(users_repository)


def _get_find_one_user_query_handler() -> FindOneUserQueryHandler:
    return FindOneUserQueryHandler(users_repository)


def _get_update_user_command_handler() -> UpdateUserCommandHandler:
    return UpdateUserCommandHandler(users_repository)


def _get_delete_user_command_handler() -> DeleteUserCommandHandler:
    return DeleteUserCommandHandler()


@users_router.post("/", status_code=CREATED)
def create_user(
    user_request: CreateUserRequest,
    handler: CreateUserCommandHandler = Depends(_get_create_user_command_handler),
) -> None:
    user = User(**user_request.model_dump())
    command = CreateUserCommand(user)
    handler.execute(command)


@users_router.get("/", status_code=OK)
def find_all_users(
    handler: FindAllUsersQueryHandler = Depends(_get_find_all_users_query_handler),
) -> UsersResponse:
    response = handler.execute()
    users: list[UserResponse] = []

    for user in response.users:
        json_user = UserResponse(**user.to_dict())
        users.append(json_user)

    return UsersResponse(users=users)


@users_router.get("/{user_id}", status_code=OK)
def find_user(
    user_id: str,
    handler: FindOneUserQueryHandler = Depends(_get_find_one_user_query_handler),
) -> UserResponse:
    handler_query = FindOneUserQuery(user_id=user_id)
    response = handler.execute(query=handler_query)
    return UserResponse(**response.user.to_dict())


@users_router.put("/{user_id}", status_code=OK)
def update_user(
    user_id: str,
    user_request: UserUpdateRequest,
    handler: UpdateUserCommandHandler = Depends(_get_update_user_command_handler),
) -> UserResponse:
    user = User(user_id, **user_request.model_dump())
    command = UpdateUserCommand(user)
    updated_user = handler.execute(command)
    return UserResponse(**updated_user.user.to_dict())


@users_router.delete("/{user_id}", status_code=NO_CONTENT)
def delete_user(
    user_id: str,
    handler: DeleteUserCommandHandler = Depends(_get_delete_user_command_handler),
) -> None:
    command = DeleteUserCommand(user_id)
    handler.execute(command)
