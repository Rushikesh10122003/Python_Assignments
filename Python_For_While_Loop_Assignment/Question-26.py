'''
ASSCII values of a characters in a string
'''
text = input("Enter a string: ")

for ch in text:
    print(ch, "=", ord(ch))