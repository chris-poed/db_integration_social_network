
import pytest
from pytest import fixture
from lib.post import Post
from lib.post_repository import PostRepository

@fixture
def seed_db(db_connection):
    return db_connection.seed("seeds/social_network.sql")

@fixture
def test_posts():
    return [
        Post(1, 'the title', 'this is some content', 14, 1),
        Post(2, 'the title', 'this is some content', 12, 1),
        Post(3, 'the title', 'this is some content', 7, 2),
        Post(4, 'the title', 'this is some content', 4, 1),
        Post(5, 'the title', 'this is some content', 9, 2),
        Post(6, 'the title', 'this is some content', 36, 1)
    ]

@fixture
def test_user_1_posts():
    return [
        Post(1, 'the title', 'this is some content', 14, 1),
        Post(2, 'the title', 'this is some content', 12, 1),
        Post(4, 'the title', 'this is some content', 4, 1),
        Post(6, 'the title', 'this is some content', 36, 1)
    ]

def test_get_all_posts(db_connection, test_posts):
    seed_db
    repository = PostRepository(db_connection)
    posts = repository.all()
    assert posts == test_posts


def test_find_posts_for_user(db_connection, test_user_1_posts):
    seed_db
    repository = PostRepository(db_connection)
    posts = repository.find(1)
    assert posts == test_user_1_posts
