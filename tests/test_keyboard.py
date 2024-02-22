from src.keyboard import Keyboard
import pytest

@pytest.fixture()
def keyboard():
    return Keyboard('Name', 2, 2, 'EN')

def test_change_lang(keyboard):
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'
