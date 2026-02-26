import pytest
from pytest import fixture, mark
from lib.user import User

@fixture
def test_user_1():
    return User(1, "test_email_address@test.com", "test_username")

@fixture
def test_user_2():
    return User(1, "test_email_address@test.com", "test_username")


"""
User constructs with an id, email_address, and username
"""

@mark.it('User instantiates with id, email_address, and username')
def test_user_constructs(test_user_1):
    assert test_user_1.id == 1
    assert test_user_1.email_address == 'test_email_address@test.com'
    assert test_user_1.username == 'test_username'


@mark.it('User object formats correctly')
def test_user_format(test_user_1):
    assert str(test_user_1) == "User(1, test_email_address@test.com, test_username)"


@mark.it('Compare two indentical users')
def test_users_are_equal(test_user_1, test_user_2):
    assert test_user_1 == test_user_2
