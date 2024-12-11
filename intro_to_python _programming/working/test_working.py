import pytest
from working import convert


def test_valid_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1 PM to 1:30 PM") == "13:00 to 13:30"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"


def test_invalid_times():
    with pytest.raises(ValueError):
        convert("13:00 AM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")  # missing space


def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")  # wrong separator
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")  # invalid 24-hour time in 12-hour format
    with pytest.raises(ValueError):
        convert("hello world")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")  # missing 'to'


if __name__ == "__main__":
    pytest.main()
