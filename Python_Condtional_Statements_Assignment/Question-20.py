'''
ticket price based on age
'''
age = int(input("Enter age: "))

if age <= 5:
    print("Ticket price: Free")
elif age <= 18:
    print("Ticket price: ₹50")
elif age <= 60:
    print("Ticket price: ₹100")
else:
    print("Ticket price: ₹60")