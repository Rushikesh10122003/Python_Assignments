'''
remove all occurrences of a given character
'''
text = input("Enter a string: ")
ch = input("Enter character to remove: ")
if len(ch) == 1:
    print("Updated string:", text.replace(ch, ""))
else:
    print("Please enter exactly one character")
