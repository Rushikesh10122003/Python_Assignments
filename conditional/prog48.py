def prog48():
    status = input("Enter result code (P=Pass, F=Fail, A=Absent, W=Withheld): ").strip().upper()
    match status:
        case "P":
            print("Result: PASS")
        case "F":
            print("Result: FAIL")
        case "A":
            print("Result: ABSENT")
        case "W":
            print("Result: WITHHELD - contact the examination office")
        case _:
            print("Invalid result code")

prog48()