'''
number is armstrong or not
'''
num = int(input("Enter a number: "))

if num < 0:
    print("Not an Armstrong number")
else:
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10

    if original == total:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")