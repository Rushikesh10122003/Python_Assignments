'''
check whether a number is strong number
'''

num = int(input("Enter a number: "))

if num < 0:
    print("Not a Strong number")
else:
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        factorial = 1

        for i in range(1, digit + 1):
            factorial = factorial * i

        total = total + factorial
        num = num // 10

    if original == total:
        print("Strong number")
    else:
        print("Not a Strong number")