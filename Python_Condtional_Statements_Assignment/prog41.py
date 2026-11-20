def prog41():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /, %): ")
    match op:
        case "+":
            print("Result:", a + b)
        case "-":
            print("Result:", a - b)
        case "*":
            print("Result:", a * b)
        case "/":
            if b == 0:
                print("Error: Division by zero")
            else:
                print("Result:", a / b)
        case "%":
            if b == 0:
                print("Error: Division by zero")
            else:
                print("Result:", a % b)
        case _:
            print("Invalid operator")
 
prog41()