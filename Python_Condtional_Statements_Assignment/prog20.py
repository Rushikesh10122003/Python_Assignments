def prog20():
    age = int(input("Enter age: "))
    if age < 0:
        print("Invalid age")
    elif age < 5:
        print("Ticket price: Free")
    elif age <= 12:
        print("Ticket price: Rs. 100")
    elif age < 60:
        print("Ticket price: Rs. 200")
    else:
        print("Ticket price: Rs. 100 (Senior citizen)")

prog20()