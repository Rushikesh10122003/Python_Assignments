'''
check palindrome list
'''

items = [1, 2, 3, 2, 1]

if items == items[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")