from abc import ABC, abstractmethod

from src.domain.user import User


class UsersRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None: ...

    @abstractmethod
    def find_all(self) -> list[User]: ...

    @abstractmethod
    def find_by_id(self, user_id: str) -> User: ...

    @abstractmethod
    def update(self, user: User) -> User: ...

    @abstractmethod
    def delete(self, user_id: str) -> None: ...
