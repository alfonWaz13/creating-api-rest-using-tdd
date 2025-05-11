from fastapi.testclient import TestClient
from http.client import CREATED

from expects import expect, equal
from doublex import Spy, Mimic
from doublex_expects import have_been_called_with

from main import app
from src.use_cases.commands.create_user_command import (
    CreateUserCommand,
    CreateUserCommandHandler,
)
from src.delivery.api.v1.users.users_router import _get_create_user_command_handler
from tests.unit.domain.user_mother import UserMother


class TestUsersRouter:
    def test_create_user(self) -> None:
        user = UserMother.get()

        command = CreateUserCommand(user)
        client = TestClient(app)
        handler = Mimic(Spy, CreateUserCommandHandler)

        app.dependency_overrides[_get_create_user_command_handler] = lambda: handler

        response = client.post("/api/v1/users", json=user.to_dict())

        expect(response.status_code).to(equal(CREATED))
        expect(handler.execute).to(have_been_called_with(command))
