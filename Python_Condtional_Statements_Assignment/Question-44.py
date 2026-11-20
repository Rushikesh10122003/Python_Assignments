'''
traffic signal 
'''
signal = input("Enter traffic signal color: ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid signal")