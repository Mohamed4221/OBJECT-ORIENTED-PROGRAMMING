# python taks 1
def simple_calculator():
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter an arithmetic operation (+, -, *, /): ").strip()

        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operation selected. Please use +, -, *, or /.")
            return

        
        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")


simple_calculator()