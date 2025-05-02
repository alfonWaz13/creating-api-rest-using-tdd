from fastapi.testclient import TestClient
from http.client import CREATED
from expects import expect, equal

from main import app


class TestUsersRouter:
    def test_create_user(self) -> None:
        payload = {"name": "Peter", "age": 42}

        client = TestClient(app)

        response = client.post("/api/v1/users", json=payload)

        expect(response.status_code).to(equal(CREATED))
