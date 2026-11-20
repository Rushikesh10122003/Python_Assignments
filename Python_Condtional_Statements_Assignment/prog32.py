def prog32():
    attendance = float(input("Enter attendance percentage: "))
    marks = float(input("Enter internal marks (out of 100): "))
    if attendance >= 75:
        if marks >= 40:
            print("Eligible for the exam")
        else:
            print("Not eligible: Internal marks are less than 40")
    else:
        print("Not eligible: Attendance is less than 75%")
 
prog32()