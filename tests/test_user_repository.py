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

def test_get_all_users(db_connection, test_users):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    users = repository.all()

    assert users == test_users

