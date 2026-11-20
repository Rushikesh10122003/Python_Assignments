def prog28():
    total = float(input("Enter total shopping amount: Rs. "))
    if total < 0:
        print("Invalid amount")
        return
    if total >= 10000:
        rate = 20
    elif total >= 5000:
        rate = 10
    elif total >= 1000:
        rate = 5
    else:
        rate = 0
    discount = total * rate / 100
    print("Discount percentage:", rate, "%")
    print("Discount amount    : Rs.", discount)
    print("Final amount to pay: Rs.", total - discount)

prog28()