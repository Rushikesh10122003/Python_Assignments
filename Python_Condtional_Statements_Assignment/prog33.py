def prog33():
    age = int(input("Enter age: "))
    salary = float(input("Enter monthly salary: Rs. "))
    credit = int(input("Enter credit score (300-900): "))
    if age >= 21 and age <= 60:
        if salary >= 25000:
            if credit >= 700:
                print("You can apply for the loan")
            else:
                print("Cannot apply: Credit score must be at least 700")
        else:
            print("Cannot apply: Monthly salary must be at least Rs. 25000")
    else:
        print("Cannot apply: Age must be between 21 and 60")
 

prog33()
