'''
Leap year or century year
'''
year = int(input("Enter a year: "))

if year % 100 == 0:
    print("Century year")
    if year % 400 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
else:
    if year % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")