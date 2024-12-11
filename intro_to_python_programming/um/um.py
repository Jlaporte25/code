import re
import sys


def main():
    try:
        print(count(input("Text: ").lower))
    except ValueError as e:
        print(e)


def count(s):
    pattern = r"\bum\b"

    matches = re.findall(pattern, s, re.IGNORECASE)

    return len(matches)


if __name__ == "__main__":
    main()
