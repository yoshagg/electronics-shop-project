from src.item import Item
import pytest


@pytest.fixture()
def stevehuys():
    return Item("stevehuys", 228, 1)


def test_item_calculate_total_price(stevehuys):
    assert stevehuys.calculate_total_price() == 228


def test_apply_discount(stevehuys):
    Item.pay_rate = 0.8
    stevehuys.apply_discount()
    assert stevehuys.price == 182.4
