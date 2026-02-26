from pytest import fixture

from lib.user import User
from lib.user_repository import UserRepository

@fixture
def test_users():
    return [
        User(1, 'johnjohnson@john.com', 'johnj'),
        User(2, 'adam@adamson.com', 'adama'),
        User(3, 'jenjennson@jenny.com', 'jennyj')
    ]

@fixture
def seed_db(db_connection):
    return db_connection.seed("seeds/social_network.sql")

def test_get_all_users(seed_db, db_connection, test_users):
    seed_db
    repository = UserRepository(db_connection)

    users = repository.all()

    assert users == test_users

def test_return_a_single_user_by_id(seed_db, db_connection, test_users):
    seed_db
    repository = UserRepository(db_connection)
    user = repository.find(3)

    assert user == test_users[2]
