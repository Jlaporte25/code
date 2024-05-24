import pytest
from plates import is_valid


def test_letters():
    assert is_valid("DK209") == True
    assert is_valid("2345") == False


def test_min_max_characters():
    assert is_valid("DKSJ12") == True
    assert is_valid("DJDNVKSKV12") == False


def test_starts_with_letters():
    assert is_valid("CDEJ12") == True
    assert is_valid("23SKF") == False


def test_ends_number():
    assert is_valid("CKEM12") == True
    assert is_valid("SFJ23D") == False


def test_start_num():
    assert is_valid("VJ321") == True
    assert is_valid("SKC001") == False


def test_punctuation():
    assert is_valid("SKC67") == True
    assert is_valid("CJS.56") == False


if __name__ == "__main__":
    pytest.main()
