import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError as e:
        print(e)


def convert(s):
    # Define the regex patterns for the expected formats
    pattern1 = r"^(\d{1,2}:\d{2} [AP]M) to (\d{1,2}:\d{2} [AP]M)$"
    pattern2 = r"^(\d{1,2} [AP]M) to (\d{1,2} [AP]M)$"

    match1 = re.match(pattern1, s)
    match2 = re.match(pattern2, s)

    if match1:
        start, end = match1.groups()
    elif match2:
        start, end = match2.groups()
    else:
        raise ValueError("Invalid format")

    # Convert both times to 24-hour format
    start_24 = to_24_hour(start)
    end_24 = to_24_hour(end)

    return f"{start_24} to {end_24}"


def to_24_hour(time_str):
    # Determine if it's in the format with or without minutes
    if ":" in time_str:
        time, period = time_str.split()
        hour, minute = map(int, time.split(":"))
    else:
        time, period = time_str.split()
        hour = int(time)
        minute = 0

    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    if not (0 <= hour < 24 and 0 <= minute < 60):
        raise ValueError("Invalid time")

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
