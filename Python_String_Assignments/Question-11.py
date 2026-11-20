'''
count how many times a character appears in a string
'''
text = input("Enter a string: ")
ch = input("Enter a character: ")
if len(ch) == 1:
    print("Occurrences:", text.count(ch))
else:
    print("Please enter exactly one character")
