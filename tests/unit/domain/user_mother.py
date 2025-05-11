from uuid import uuid4

from src.domain.user import User


class UserMother:
    @staticmethod
    def get() -> User:
        return User(
            id=str(uuid4()),
            name="John",
            age=42,
        )
