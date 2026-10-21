def prog31():
    n = int(input("Enter a number: "))
    if n > 0:
        if n % 2 == 0:
            print(n, "is Positive and Even")
        else:
            print(n, "is Positive but Odd")
    else:
        print(n, "is not a positive number")
 
prog31()