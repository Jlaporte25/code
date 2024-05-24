import sys


def main():
    try:
        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit
        elif len(sys.argv) == 1:
            print("Too few command-line arguments")
            sys.exit
        else:
            filename = sys.argv[1]
            lines = read_file(filename)
            print(lines)

    except FileNotFoundError:
        if FileNotFoundError and sys.argv[1].endswith(".py"):
            print("File does not exist")
            sys.exit
        elif FileNotFoundError and not sys.argv[1].endswith(".py"):
            print("Not a Python file")
            sys.exit


def read_file(file):
    with open(file, "r") as f:
        code = f.readlines()
        no_white = str(code)
        lines = len(code)
        f.close()
    return lines


if __name__ == "__main__":
    main()
