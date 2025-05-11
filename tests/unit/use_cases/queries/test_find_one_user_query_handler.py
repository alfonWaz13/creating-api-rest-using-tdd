from doublex import Mimic, Stub
from expects import expect, equal

from src.use_cases.queries.find_one_user_query import (
    FindOneUserQueryHandler,
    FindOneUserQuery,
)
from src.infraestructure.in_memory.users_repository import InMemoryUsersRepository
from tests.unit.domain.user_mother import UserMother


class TestFindOneUserQueryHandler:
    def test_find_one_user(self) -> None:
        mocked_user = UserMother.get()
        with Mimic(Stub, InMemoryUsersRepository) as users_repository:
            users_repository.find_one(mocked_user.id).returns(mocked_user)
            handler = FindOneUserQueryHandler(users_repository)
        query = FindOneUserQuery(mocked_user.id)

        response = handler.execute(query=query)

        user = response.user
        expect(user).to(equal(mocked_user))
