import sys
import os


def main():
    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <filename.py>")

    # Get the filename from the command-line arguments
    filename = sys.argv[1]

    # Check if the file has a .py extension
    if not filename.endswith(".py"):
        sys.exit("Error: The file must have a .py extension")

    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit("Error: The file does not exist")

    try:
        # Open the file and read its lines
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        code_lines = 0

        for line in lines:
            stripped_line = line.strip()
            # Skip blank lines and lines that start with a comment
            if stripped_line and not stripped_line.startswith("#"):
                code_lines += 1

        print(f"Number of lines of code: {code_lines}")

    except Exception as e:
        sys.exit(f"Error: {e}")


if __name__ == "__main__":
    main()
