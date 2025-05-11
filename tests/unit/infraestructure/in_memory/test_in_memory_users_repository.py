from expects import expect, equal

from src.infraestructure.in_memory.users_repository import InMemoryUsersRepository
from tests.unit.domain.user_mother import UserMother


class TestInMemoryUserRepository:
    def test_save_user(self) -> None:
        user = UserMother.get()
        repository = InMemoryUsersRepository()

        repository.save(user)
        users = repository.find_all()

        expect(users).to(equal([user]))
