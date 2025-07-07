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

def percentage(number, percent):
    """
    Calculate the percentage of a number.
    
    Args:
        number: The base number
        percent: The percentage value (e.g., 20 for 20%)
    
    Returns:
        The percentage of the given number
    """
    return (percent / 100) * number

# Example usage:
result = calculator('+', 10, 5)  # Returns 15
print(result)

result = percentage(100, 20)  # Returns 20
print(result)

print('this is a demo for empire')
print('this is a demo for empire 2')