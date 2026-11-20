'''
find the index of a given character in a string
'''
text = input("Enter a string: ")
ch = input("Enter a character: ")
if len(ch) == 1:
    print("Index:", text.find(ch))
else:
    print("Please enter exactly one character")
