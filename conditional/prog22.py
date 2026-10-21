def prog22():
    salary = float(input("Enter salary: "))
    years = int(input("Enter years of service: "))
    if years > 10:
        bonus = salary * 0.20
    elif years >= 5:
        bonus = salary * 0.10
    elif years >= 2:
        bonus = salary * 0.05
    else:
        bonus = 0
    print("Bonus amount: Rs.", bonus)
    print("Total salary with bonus: Rs.", salary + bonus)


prog22()