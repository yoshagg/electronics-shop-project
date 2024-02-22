import pytest
from src.phone import Phone

@pytest.fixture()
def object():
    return Phone('Apple', 2, 2, 2)


def test_repr(object):
    assert repr(object) == "Phone('Apple', 2, 2, 2)"


def test_str(object):
    assert str(object) == 'Apple'


def test_number_of_sim(object):
    assert object.number_of_sim == 2

