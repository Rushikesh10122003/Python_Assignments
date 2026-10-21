def prog29():
    age = int(input("Enter age: "))
    weight = float(input("Enter weight (kg): "))
    if age >= 18 and age <= 65 and weight >= 50:
        print("Eligible to donate blood")
    else:
        print("Not eligible to donate blood")
        if age < 18 or age > 65:
            print("Reason: Age must be between 18 and 65")
        if weight < 50:
            print("Reason: Weight must be at least 50 kg")

prog29()