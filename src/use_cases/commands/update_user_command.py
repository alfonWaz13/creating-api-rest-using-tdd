from dataclasses import dataclass

from src.domain.user import User
from src.domain.users_repository import UsersRepository


@dataclass
class UpdateUserCommand:
    user: User


@dataclass
class UpdateUserCommandResponse:
    user: User


class UpdateUserCommandHandler:
    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository

    def execute(self, command: UpdateUserCommand) -> UpdateUserCommandResponse:
        user = command.user
        self.users_repository.update(user)
        return UpdateUserCommandResponse(user)
