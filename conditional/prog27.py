def prog27():
    # Stored (correct) credentials
    saved_user = "admin"
    saved_pass = "admin123"
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == saved_user and password == saved_pass:
        print("Login Successful")
    elif username != saved_user:
        print("Login Failed: Invalid username")
    else:
        print("Login Failed: Incorrect password")

prog27()