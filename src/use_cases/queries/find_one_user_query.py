from dataclasses import dataclass

from src.domain.user import User
from src.domain.users_repository import UsersRepository


@dataclass
class FindOneUserQueryResponse:
    user: User


class FindOneUserQueryHandler:
    def __init__(self, users_repository: UsersRepository) -> None:
        self.users_repository = users_repository

    def execute(self, user_id: str) -> FindOneUserQueryResponse:
        user = self.users_repository.find_one(user_id=user_id)
        return FindOneUserQueryResponse(user=user)
