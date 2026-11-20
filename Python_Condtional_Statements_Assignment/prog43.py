def prog43():
    signal = input("Enter signal colour (red/yellow/green): ").strip().lower()
    match signal:
        case "red":
            print("STOP")
        case "yellow":
            print("GET READY / SLOW DOWN")
        case "green":
            print("GO")
        case _:
            print("Invalid signal colour")
 
prog43()