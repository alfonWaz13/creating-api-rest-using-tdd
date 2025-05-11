from dataclasses import dataclass

from src.domain.user import User


@dataclass
class FindAllUsersQueryResponse:
    users: list[User]


class FindAllUsersQueryHandler:
    def execute(self) -> FindAllUsersQueryResponse:
        return FindAllUsersQueryResponse(users=[])
