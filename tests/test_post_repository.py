
import pytest
from pytest import fixture, mark
from lib.post import Post
from lib.post_repository import PostRepository

@fixture(autouse=True)
def seed_db(db_connection):
    db_connection.seed("seeds/social_network.sql")

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

@fixture
def test_user_3_new_post():
    return [Post(7, 'the title', 'this is some content', 7, 3)]

@mark.it('Get all posts for all users')
def test_get_all_posts(db_connection, test_posts):
    repository = PostRepository(db_connection)
    posts = repository.all()
    assert posts == test_posts

@mark.it('Find all posts for user 1')
def test_find_posts_for_user(db_connection, test_user_1_posts):
    repository = PostRepository(db_connection)
    posts = repository.find(1)
    assert posts == test_user_1_posts

@mark.it('Create a new post for user 3')
def test_create_post_for_user(db_connection, test_user_3_new_post):
    repository = PostRepository(db_connection)
    repository.create(Post(None, 'the title', 'this is some content', 7, 3))
    result = repository.find(3)
    assert result == test_user_3_new_post

@mark.it('Find all posts with a given username')
def test_find_posts_by_username(db_connection, test_user_1_posts):  
    seed_db
    repository = PostRepository(db_connection)
    posts = repository.find_with_username('johnj')
    assert posts == test_user_1_posts
