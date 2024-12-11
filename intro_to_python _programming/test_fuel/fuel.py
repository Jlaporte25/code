def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        if x > y:
            raise ValueError("Numerator cannot be greater than denominator")

        percentage = round((x / y) * 100)

        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage out of range")

        return percentage

    except ValueError:
        raise ValueError("Invalid input: X and Y must be integers and in the form X/Y")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    fraction = input("Enter a fraction (X/Y): ").strip()
    try:
        percentage = convert(fraction)
        print("Percentage:", percentage)
        print("Gauge:", gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
