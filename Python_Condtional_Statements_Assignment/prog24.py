def prog24():
    marks = float(input("Enter percentage (0-100): "))
    if marks < 0 or marks > 100:
        print("Invalid marks")
    elif marks >= 75:
        print("Result: Distinction")
    elif marks >= 60:
        print("Result: First Class")
    elif marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

prog24()