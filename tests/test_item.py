from src.item import Item
import pytest


@pytest.fixture()
def object():
    return Item("object", 228, 1)


def test_repr(object):
    assert repr(object) == '''Item('object', 228, 1)'''


def test_item_calculate_total_price(object):
    assert object.calculate_total_price() == 228


def test_apply_discount(object):
    Item.pay_rate = 0.8
    object.apply_discount()
    assert object.price == 182.4


def test_instantiate_from_csv():
    assert Item.instantiate_from_csv('../src/items.csv') == None


def test_string_to_number():
    assert Item.string_to_number("20") == 20
    assert Item.string_to_number("2.0") == 2
    assert Item.string_to_number("2.5") == 2
