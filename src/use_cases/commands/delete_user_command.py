from dataclasses import dataclass


@dataclass
class DeleteUserCommand:
    user_id: str


class DeleteUserCommandHandler:
    def execute(self, command: DeleteUserCommand) -> None:
        raise NotImplementedError()
