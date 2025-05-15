from dataclasses import dataclass

from src.domain.user import User


@dataclass
class UpdateUserCommand:
    user: User


@dataclass
class UpdateUserCommandResponse:
    user: User


class UpdateUserCommandHandler:
    def execute(self, command: UpdateUserCommand) -> UpdateUserCommandResponse:
        raise NotImplementedError()
