import emoji

def main():
    em = input()
    emojized = emoji.emojize(em, language='alias')
    print(emojized)

if __name__ == "__main__":
    main()
