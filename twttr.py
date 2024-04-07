def main():
    tweet = input("Input: ").strip()
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    result = ""
    
    for ch in tweet:
        if ch not in vowels:
            result = result + ch
    
    print(result)        

main()