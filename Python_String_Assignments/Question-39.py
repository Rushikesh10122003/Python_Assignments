'''
check whether a string is a valid identifier
'''
text = input("Enter a string: ")
if text.isidentifier():
    print("Valid Python identifier")
else:
    print("Invalid Python identifier")
