from datetime import date
import inflect
import sys


def main():
    dob = input("Date of Birth (YYYY-MM-DD): ")
    try:
        year, month, day = map(int, dob.split("-"))
        birth_date = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date format. Please use YYYY-MM-DD.")

    today = date.today()
    if birth_date > today:
        sys.exit("Date of birth cannot be in the future.")

    age_in_minutes = calculate_age_in_minutes(birth_date, today)
    age_in_words = convert_number_to_words(age_in_minutes)

    print(f"{age_in_words} minutes")


def calculate_age_in_minutes(birth_date, today):
    delta = today - birth_date
    return delta.days * 24 * 60


def convert_number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number).replace(",", "")


if __name__ == "__main__":
    main()
