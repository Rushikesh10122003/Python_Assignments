def prog14():
    ch = input("Enter a character: ")
    if len(ch) != 1 or not ch.isalpha():
        print("Please enter a single alphabet character")
    elif ch.isupper():
        print("The character is Uppercase")
    else:
        print("The character is Lowercase")

prog14()