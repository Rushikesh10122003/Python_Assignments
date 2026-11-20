'''
find first and last occurrence of a character
'''
text = input("Enter a string: ")
ch = input("Enter a character: ")
if len(ch) == 1:
    first = text.find(ch)
    last = text.rfind(ch)
    if first == -1:
        print("Character not found")
    else:
        print("First occurrence index:", first)
        print("Last occurrence index:", last)
else:
    print("Please enter exactly one character")
