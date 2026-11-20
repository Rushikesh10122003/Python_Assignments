'''
simple ATM
'''
balance = 10000

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Balance: ", balance)

    case 2:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance = balance + amount
            print("Deposited successfully")
            print("Updated balance: ", balance)
        else:
            print("Invalid amount")

    case 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
            print("Remaining balance: ", balance)
        elif amount <= 0:
            print("Invalid amount")
        else:
            print("Insufficient balance")

    case _:
        print("Invalid choice")