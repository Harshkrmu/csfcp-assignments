def calculator():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                return "Error: Cannot divide by zero."
            result = num1 / num2
        else:
            return "Invalid operation."

        return f"Result: {result}"

    except ValueError:
        return "Invalid input. Please enter numbers only."


print(calculator())
