import random


def main():
    while True:
        try:
            n = int(input("Level: "))
            answer = random.randrange(1, n)
            break
        except ValueError:
            continue
    while True:
        try:
            guess = int(input("Guess: "))
            if guess == answer:
                print("Just Right!")
                break
            elif guess > answer:
                print("Too large!")
            elif guess < answer:
                print("Too small!")
        except ValueError:
            continue


if __name__ == "__main__":
    main()
