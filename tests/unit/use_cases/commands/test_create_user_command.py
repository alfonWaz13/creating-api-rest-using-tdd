from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect

from src.infraestructure.in_memory.users_repository import InMemoryUsersRepository
from src.use_cases.commands.create_user_command import (
    CreateUserCommand,
    CreateUserCommandHandler,
)
from tests.unit.domain.user_mother import UserMother


class TestCreateUserCommandHandler:
    def test_create_user_command_handler(self) -> None:
        user = UserMother.get()
        command = CreateUserCommand(user)
        users_repository = Mimic(Spy, InMemoryUsersRepository)
        handler = CreateUserCommandHandler(users_repository)

        handler.execute(command)

        expect(users_repository.save).to(have_been_called_with(user))
