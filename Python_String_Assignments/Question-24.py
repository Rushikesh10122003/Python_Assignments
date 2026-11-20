'''
extract only digits from a string
'''
text = input("Enter a string: ")
digits = ""
for ch in text:
    if ch.isdigit():
        digits += ch
print("Digits:", digits)
