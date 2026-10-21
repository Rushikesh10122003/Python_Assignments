def prog34():
    year = int(input("Enter a year: "))
    is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    is_century = (year % 100 == 0)
    if is_leap and is_century:
        print(year, "is a Leap Year and also a Century Year")
    elif is_leap:
        print(year, "is a Leap Year but not a Century Year")
    elif is_century:
        print(year, "is a Century Year but not a Leap Year")
    else:
        print(year, "is neither a Leap Year nor a Century Year")

prog34()