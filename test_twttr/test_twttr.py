import pytest
from twttr import shorten


def test_shor():
    assert shorten("Jacob") == "Jcb"


def test_hello():
    assert shorten("Hello") == "Hll"


def test_goodbye():
    assert shorten("Goodbye") == "Gdby"
    assert shorten("Bye") == "By"


def test_numbers():
    assert shorten("3 is less than 5") == "3 s lss thn 5"


def test_punc():
    assert shorten("Do you mean that?") == "D y mn tht?"


def test_capital():
    assert shorten("Of course!") == "f crs!"


if __name__ == "__main__":
    pytest.main
