import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

    global characters
    characters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_valid(s):
    if (
        start_with_letters(s)
        and min_max_characters(s)
        and ends_with_numbers(s)
        and starting_number(s)
        and check_punctuation(s)
    ):
        return True
    else:
        return False


def min_max_characters(n):
    if len(n) >= 2 and len(n) <= 6:
        return True
    else:
        return False


def start_with_letters(s):
    sn = s[0:2]
    if sn.isalpha():
        return True
    else:
        return False


def ends_with_numbers(j):
    numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    if j.endswith(numbers):
        return True
    else:
        return False


def starting_number(n):
    s = n.lstrip("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if s.startswith("0"):
        return False
    else:
        return True


def check_punctuation(s):
    return not bool(re.search(r"[!\"#$%&'()*+,-./:;<=>?@[\]^_` {|}~]", s))


if __name__ == "__main__":
    main()
