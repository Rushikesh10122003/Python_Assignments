def prog17():
    marks = float(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks")
    elif marks >= 75:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B")
    elif marks >= 40:
        print("Grade: C")
    else:
        print("Grade: Fail")


prog17()
