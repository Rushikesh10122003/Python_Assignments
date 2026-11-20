def prog38():
    subjects = 5
    passed_all = True
    for i in range(1, subjects + 1):
        m = float(input(f"Enter marks of subject {i}: "))
        if m < 40:
            passed_all = False
    if passed_all:
        print("Student has passed in all subjects")
    else:
        print("Student has failed in one or more subjects")

prog38()