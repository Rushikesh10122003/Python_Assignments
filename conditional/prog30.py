def prog30():
    n = abs(int(input("Enter a number: ")))
    if n < 10:
        print("Single digit number")
    elif n < 100:
        print("Double digit number")
    elif n < 1000:
        print("Three digit number")
    else:
        print("Number has more than three digits")

prog30()