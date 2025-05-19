from doublex import Mimic, Spy
from expects import expect
from doublex_expects import have_been_called_with

from src.infraestructure.in_memory.users_repository import InMemoryUsersRepository
from src.use_cases.commands.delete_user_command import (
    DeleteUserCommand,
    DeleteUserCommandHandler,
)


class TestDeleteUserCommand:
    def test_delete_user(self) -> None:
        user_id = "user_id"
        repository = Mimic(Spy, InMemoryUsersRepository)
        command = DeleteUserCommand(user_id)
        handler = DeleteUserCommandHandler(repository)

        handler.execute(command)

        expect(repository.delete).to(have_been_called_with(user_id))
