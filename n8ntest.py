def calculator(operation, num1, num2):

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Use '+', '-', '*', or '/'")

# Example usage:
result = calculator('+', 10, 5)  # Returns 15
print(result)
