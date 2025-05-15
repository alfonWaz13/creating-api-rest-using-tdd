from expects import expect, equal

from src.domain.user import User
from src.infraestructure.in_memory.users_repository import InMemoryUsersRepository
from tests.unit.domain.user_mother import UserMother


class TestInMemoryUserRepository:
    def test_save_user(self) -> None:
        user = UserMother.get()
        repository = InMemoryUsersRepository()

        repository.save(user)
        users = repository.find_all()

        expect(users).to(equal([user]))

    def test_save_and_find_all_users(self) -> None:
        user_1 = UserMother.get()
        user_2 = UserMother.get()
        repository = InMemoryUsersRepository()

        repository.save(user_1)
        repository.save(user_2)
        users = repository.find_all()

        expect(users).to(equal([user_1, user_2]))

    def test_save_and_find_one_user(self) -> None:
        user = UserMother.get()
        repository = InMemoryUsersRepository()

        repository.save(user)
        user_retrieved = repository.find_by_id(user.id)

        expect(user_retrieved).to(equal(user))

    def test_save_and_update_one_user(self) -> None:
        user = UserMother.get()
        new_user = User(user.id, user.name, user.age + 1)

        repository = InMemoryUsersRepository()
        repository.save(user)
        updated_user = repository.update(new_user)
        users = repository.find_all()

        expect(users).to(equal([updated_user]))
