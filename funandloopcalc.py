def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero!"
    return num1 / num2

def calculator():
    while True:
        print("======================")
        print("Select your operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        print("======================")

        op = int(input(">>> "))

        if op == 5:
            print("Goodbye Baanbil!")
            break

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if op == 1:
            print(f"Result: {add(num1, num2)}")
        elif op == 2:
            print(f"Result: {subtract(num1, num2)}")
        elif op == 3:
            print(f"Result: {multiply(num1, num2)}")
        elif op == 4:
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid option!")

calculator()
