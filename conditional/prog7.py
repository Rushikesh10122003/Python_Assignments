def prog7():
    ch = input("Enter a character: ").lower()
    if len(ch) != 1 or not ch.isalpha():
        print("Please enter a single alphabet character")
    elif ch in "aeiou":
        print("The character is a Vowel")
    else:
        print("The character is a Consonant")

prog7()