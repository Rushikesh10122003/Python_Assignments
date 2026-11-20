'''
Login status based on username and password using if-else statements.
'''
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin":
    print("Login successful")
else:
    print("Invalid username or password")