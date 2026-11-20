'''
check whether a string starts with a given substring
'''
text = input("Enter a string: ")
sub = input("Enter substring: ")
if text.startswith(sub):
    print("String starts with the given substring")
else:
    print("String does not start with the given substring")
