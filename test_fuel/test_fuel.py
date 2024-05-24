import pytest
from fuel import (
    convert,
    gauge,
)  # Adjust the import statement according to your module name


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("2/5") == 40
    assert convert("1/1") == 100
    assert convert("0/1") == 0


def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("1.5/2.5")
    with pytest.raises(ValueError):
        convert("2/1")  # Numerator greater than denominator
    with pytest.raises(ValueError):
        convert("1/")  # Missing denominator
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"


if __name__ == "__main__":
    pytest.main()
