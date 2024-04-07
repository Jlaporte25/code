def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    
    
    
    global characters        
    characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


    

def is_valid(s):
    if start_with_letters(s) and min_max_characters(s): 
       return True
    else:
       return False



def min_max_characters(n):
    if len(n) >= 2 and len(n) <= 6:
        return True
    else:
        return False
        
def start_with_letters(s):
    characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    s = s[0:2]
    s = s.split(" ,")
    while True:
        if s in characters:
            print(s)
            return True
        else:
            print(s)
            return False
        
    
main()