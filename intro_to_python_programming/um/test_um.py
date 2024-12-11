import pytest
from um import count


def test_valid():
    assert count("hello, um, world.") == 1
    assert count("hello, world") == 0
    assert count("I, um think you um, need to do the dishes.") == 2


def test_case():
    assert count("Um, what's up?") == 1
    assert count("Um that's so funny. Um, I love it.") == 2


def test_um_in_words():
    assert count("the clumsy drummer said um, no.") == 1
    assert count("Um that's a dumb thing to say.") == 1


if __name__ == "__main__":
    pytest.main()
