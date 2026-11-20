'''
check weather a person can apply for loan
'''
age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))

if age >= 21:
    if salary >= 25000:
        print("Eligible to apply for a loan")
    else:
        print("Not eligible: salary too low")
else:
    print("Not eligible: age requirement not met")