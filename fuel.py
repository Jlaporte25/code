while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split(sep="/")
        z = int(x)/int(y)
        z = float(z) * 100
        z = round(z)
        print(z)
        if z <= 100:
            break
        
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

if z >= 99 and z <= 100:
    print("F")
elif z <= 1:
    print("E")
else:
    print(f"{z}%")