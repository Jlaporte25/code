import inflect

def main():
    p = inflect.engine()
    while True:
        try:
            name = input("Name: ")
            mylist = p.join(name)
        except:
            print(f"Adieu, Adieu, to {mylist}")


if __name__ == "__main__":
    main()
