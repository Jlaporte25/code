def main():
    # Prompt the user for input
    text = input("Input: ")

    # Remove vowels from the input text
    result = shorten(text)

    # Output the result
    print(result)


# Define the function to remove vowels
def shorten(text):
    # Define the vowels to remove
    vowels = "AEIOUaeiou"

    # Create a new string with vowels removed
    result = ""
    for char in text:
        if char not in vowels:
            result += char

    return result


if __name__ == "__main__":
    main()
