import sys
import csv
import os


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: Python3 scourgify.py <filename1.csv> <filename2.csv>")

    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    if not filename1.endswith(".csv") or not filename2.endswith(".csv"):
        sys.exit("not a csv file")

    if not os.path.isfile(filename1):
        sys.exit("file does not exist")

    with open(filename1, "r") as input_file:
        reader = csv.reader(input_file)
        header = next(reader)
        data = []
        for row in reader:
            name, house = row
            last_name, first_name = name.split(", ")
            data.append([first_name, last_name, house])

    with open(filename2, "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["first", "last", "house"])
        writer.writerows(data)


if __name__ == "__main__":
    main()
