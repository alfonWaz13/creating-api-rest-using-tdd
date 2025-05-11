import pytest
from fastapi.testclient import TestClient
from http.client import CREATED, OK

from expects import expect, equal
from doublex import Spy, Mimic, Stub
from doublex_expects import have_been_called_with

from main import app
from src.use_cases.commands.create_user_command import (
    CreateUserCommand,
    CreateUserCommandHandler,
)
from src.delivery.api.v1.users.users_router import (
    _get_create_user_command_handler,
    _get_find_all_users_query_handler,
)
from src.use_cases.queries.find_all_users_query import (
    FindAllUsersQueryHandler,
    FindAllUsersQueryResponse,
)
from tests.unit.domain.user_mother import UserMother


class TestUsersRouter:
    @pytest.fixture(autouse=True)
    def client(self) -> TestClient:
        return TestClient(app)

    def test_create_user(self, client: TestClient) -> None:
        user = UserMother.get()

        command = CreateUserCommand(user)
        handler = Mimic(Spy, CreateUserCommandHandler)

        app.dependency_overrides[_get_create_user_command_handler] = lambda: handler

        response = client.post("/api/v1/users", json=user.to_dict())

        expect(response.status_code).to(equal(CREATED))
        expect(handler.execute).to(have_been_called_with(command))

    def test_find_all_users(self, client: TestClient) -> None:
        user = UserMother.get()
        with Mimic(Stub, FindAllUsersQueryHandler) as handler:
            query_response = FindAllUsersQueryResponse(users=[user])
            handler.execute().returns(query_response)
        app.dependency_overrides[_get_find_all_users_query_handler] = lambda: handler

        response = client.get("/api/v1/users")

        expect(response.status_code).to(equal(OK))
        expect(response.json()).to(equal({"users": [user.to_dict()]}))
