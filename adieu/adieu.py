import inflect


def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            mylist = p.join(names)
            print(f"Adieu, Adieu, to {mylist}")
            break


if __name__ == "__main__":
    main()
