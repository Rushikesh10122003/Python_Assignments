'''
calculate power of a number without using pow()
'''

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
result = 1

if exponent < 0:
    print("Enter a non-negative exponent")
else:
    for i in range(exponent):
        result = result * base

    print("Result:", result)