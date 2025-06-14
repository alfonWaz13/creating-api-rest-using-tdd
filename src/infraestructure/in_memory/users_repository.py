from src.domain.user import User
from src.domain.users_repository import UsersRepository


class InMemoryUsersRepository(UsersRepository):
    def __init__(self) -> None:
        self._users: dict[str, User] = {}

    def save(self, user: User) -> None:
        self._users[user.id] = user

    def find_all(self) -> list[User]:
        return list(self._users.values())

    def find_by_id(self, user_id: str) -> User:
        return self._users[user_id]

    def update(self, user: User) -> User:
        self._users[user.id] = user
        return user

    def delete(self, user_id: str) -> None:
        self._users.pop(user_id)
