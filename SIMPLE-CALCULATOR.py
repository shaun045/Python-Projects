print("=== WELCOME TO SIMPLE CALCULATOR ===")

calculation_count = 0

while True:
    try:
        num1 = float(input("Enter first number: "))

    except ValueError:
        print("Invalid input! Must be numbers")
        continue

    operation = ["+", "-", "*", "/"]
    op = input("Enter your operation: ")
    if op not in operation:
        print("Please enter valid input")
        continue

    try:
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Invalid input! Must be numbers")
        continue

    if op == "+":
        result = num1 + num2
        print(f"{num1} {op} {num2} -> {result:.2f}")

    elif op == "-":
        result = num1 - num2
        print(f"{num1} {op} {num2} -> {result:.2f}")

    elif op == "*":
        result = num1 * num2
        print(f"{num1} {op} {num2} -> {result}")

    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
            continue
        else:
            result = num1/num2
            print(f"{num1} {op} {num2} -> {result}")

    else:
        print("Please enter valid input!")

    calculation_count += 1

    again = input("Would you like to use the calculator again (y/n)? ").lower()
    if again == "n":
        print("Alright, see you next time!")
    elif again == "y":
        continue
    else:
        print("Please enter valid input")
        continue
