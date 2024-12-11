import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regular expression pattern to match IPv4 address
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)

    if not match:
        return False

    # Check if each octet is between 0 and 255
    for group in match.groups():
        if not 0 <= int(group) <= 255:
            return False

    return True


if __name__ == "__main__":
    main()
