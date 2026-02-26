import pytest
from pytest import fixture, mark
from lib.post import Post


@fixture
def test_post_1():
    return Post(1, 'Test title', 'Test content', 1, 1)

@fixture
def test_post_2():
    return Post(1, 'Test title', 'Test content', 1, 1)


@mark.it('Post instantiates with id, title, content, views, and user_id')
def test_post_construct(test_post_1):
    assert test_post_1.id == 1
    assert test_post_1.title == 'Test title'
    assert test_post_1.content == 'Test content'
    assert test_post_1.views == 1
    assert test_post_1.user_id == 1


@mark.it('Post object formats correctly')
def test_post_format(test_post_1):
    assert str(test_post_1) == "Post(1, Test title, Test content, 1, 1)"

@mark.it('Compare two indentical posts')
def test_posts_are_equal(test_post_1, test_post_2):
    assert test_post_1 == test_post_2