from doublex import Mimic, Spy
from expects import expect
from doublex_expects import have_been_called_with

from src.infraestructure.in_memory.users_repository import InMemoryUsersRepository
from src.use_cases.commands.update_user_command import (
    UpdateUserCommand,
    UpdateUserCommandHandler,
)
from tests.unit.domain.user_mother import UserMother


class TestUpdateUserCommandHandler:
    def test_update_command_handler(self) -> None:
        user = UserMother.get()
        users_repository = Mimic(Spy, InMemoryUsersRepository)
        command = UpdateUserCommand(user)
        handler = UpdateUserCommandHandler(users_repository)

        handler.execute(command)

        expect(users_repository.update).to(have_been_called_with(user))
