def prog49():
    balance = 10000.0
    while True:
        print("\n------ ATM MENU ------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                print("Current balance: Rs.", balance)
            case 2:
                amt = float(input("Enter amount to deposit: Rs. "))
                if amt > 0:
                    balance += amt
                    print("Deposited successfully. New balance: Rs.", balance)
                else:
                    print("Invalid amount")
            case 3:
                amt = float(input("Enter amount to withdraw: Rs. "))
                if amt <= 0:
                    print("Invalid amount")
                elif amt > balance:
                    print("Insufficient balance")
                else:
                    balance -= amt
                    print("Please collect your cash. New balance: Rs.", balance)
            case 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            case _:
                print("Invalid choice")
 
prog49()