from validator_collection import validators


def main():
    print(valid_email(input("What's your email address? ")))


def valid_email(s):
    try:
        if validators.email(s):
            return "Valid"
    except ValueError:
        return "Invalid"


if __name__ == "__main__":
    main()
