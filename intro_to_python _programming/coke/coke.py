def main():
    global amount_due
    amount_due = int(50)
    
    while True:
        if amount_due > 0:
            inserted_coin = int(input("Insert Coin: "))
            due(inserted_coin)
        elif amount_due <= 0:
            print("Change Owed: "+str(abs(amount_due)))
            break

    
def due(n):
    while True:
        global amount_due
        if n == 25 or n == 10 or n == 5:
           amount_due = amount_due - n
        if amount_due > 0:
            print("Amount Due: "+str(amount_due))
        break
main()