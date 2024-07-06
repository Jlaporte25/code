import pytest
from datetime import date
from seasons import calculate_age_in_minutes, convert_number_to_words


def test_calculate_age_in_minutes():
    birth_date = date(2000, 1, 1)
    today = date(2020, 1, 1)
    assert calculate_age_in_minutes(birth_date, today) == 10540800

    birth_date = date(2000, 2, 29)
    today = date(2021, 2, 28)
    assert calculate_age_in_minutes(birth_date, today) == 11037600


def test_convert_number_to_words():
    assert (
        convert_number_to_words(10540800)
        == "ten million five hundred forty thousand eight hundred minutes"
    )
    assert (
        convert_number_to_words(11037600)
        == "eleven million thirty-seven thousand six hundred minutes"
    )


if __name__ == "__main__":
    pytest.main()
