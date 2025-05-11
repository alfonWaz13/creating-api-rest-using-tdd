from doublex import Mimic, Stub
from expects import expect, equal

from src.infraestructure.in_memory.users_repository import InMemoryUsersRepository
from src.use_cases.queries.find_all_users_query import FindAllUsersQueryHandler
from tests.unit.domain.user_mother import UserMother


class TestFindAllUsersQueryHandler:
    def test_find_all_users(self) -> None:
        mocked_user = UserMother.get()

        with Mimic(Stub, InMemoryUsersRepository) as users_repository:
            users_repository.find_all().returns([mocked_user])
            handler = FindAllUsersQueryHandler(users_repository)

        response = handler.execute()
        users = response.users

        expect(users).to(equal([mocked_user]))
