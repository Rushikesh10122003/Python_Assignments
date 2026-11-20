'''
remove duplicates
'''

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 4, 7]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)