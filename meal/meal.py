def main():
    time = input("What time is it? ")
    meal_time = convert(time)

    if meal_time >= 7 and meal_time <= 8:
        print("breakfast time")
    elif meal_time >= 12 and meal_time <= 13:
        print("lunch time")
    elif meal_time >= 18 and meal_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    int(hours)
    int(minutes)
    minutes = int(minutes) / 60
    new_time = float(hours) + float(minutes)
    return new_time

if __name__ == "__main__":
    main()