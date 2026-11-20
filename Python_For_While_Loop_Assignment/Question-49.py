'''
display menu-driven program using while loop
'''

while True:
    print("\n--- MENU ---")
    print("1. Print numbers from 1 to 10")
    print("2. Print even numbers from 1 to 20")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for i in range(1, 11):
            print(i)

    elif choice == 2:
        for i in range(2, 21, 2):
            print(i)

    elif choice == 3:
        print("Program exited")
        break

    else:
        print("Invalid choice")