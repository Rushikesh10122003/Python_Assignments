'''
extract only alphabets from a string
'''
text = input("Enter a string: ")
alphabets = ""
for ch in text:
    if ch.isalpha():
        alphabets += ch
print("Alphabets:", alphabets)
