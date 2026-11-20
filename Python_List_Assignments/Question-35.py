
'''
remove all even numbers
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print(odd_numbers)
