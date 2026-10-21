def prog45():
    grade = input("Enter grade (A/B/C/D/F): ").strip().upper()
    match grade:
        case "A":
            print("Excellent")
        case "B":
            print("Very Good")
        case "C":
            print("Good")
        case "D":
            print("Satisfactory")
        case "F":
            print("Fail - Better luck next time")
        case _:
            print("Invalid grade")

prog45()