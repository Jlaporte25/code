import csv
import sys
import os
from tabulate import tabulate


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py <filename.csv>")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("not a csv file")

    if not os.path.isfile(filename):
        sys.exit("file does not exist")

    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
        print(tabulate(data, headers="firstrow", tablefmt="grid"))
        csvfile.close()


if __name__ == "__main__":
    main()
