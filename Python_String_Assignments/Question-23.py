'''
check whether a string is a palindrome
'''
text = input("Enter a string: ")
clean = text.lower().replace(" ", "")
if clean == clean[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome string")
