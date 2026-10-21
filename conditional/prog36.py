def prog36():
    age = int(input("Enter age: "))
    test = input("Have you passed the driving test? (yes/no): ").strip().lower()
    if age >= 18:
        if test == "yes":
            print("Eligible for a driving license")
        else:
            print("Not eligible: You must pass the driving test")
    else:
        print("Not eligible: Minimum age is 18")
prog36()