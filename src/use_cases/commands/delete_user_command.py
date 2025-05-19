from dataclasses import dataclass

from src.domain.users_repository import UsersRepository


@dataclass
class DeleteUserCommand:
    user_id: str


class DeleteUserCommandHandler:
    def __init__(self, repository: UsersRepository) -> None:
        self.repository = repository

    def execute(self, command: DeleteUserCommand) -> None:
        self.repository.delete(command.user_id)
