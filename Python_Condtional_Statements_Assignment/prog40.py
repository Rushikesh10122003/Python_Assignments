def prog40():
    pwd = input("Enter password: ")
    if len(pwd) >= 8:
        if any(c.isdigit() for c in pwd):
            if any(c.isupper() for c in pwd):
                if any(not c.isalnum() for c in pwd):
                    print("Valid password")
                else:
                    print("Invalid: Must contain a special character")
            else:
                print("Invalid: Must contain an uppercase letter")
        else:
            print("Invalid: Must contain a digit")
    else:
        print("Invalid: Must be at least 8 characters long")

prog40()