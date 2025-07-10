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

    return (percent / 100) * number



def square_number(number):

    return number * number


### newly added function
def cube_number(number):
    return number * number * number




result = calculator('+', 10, 5)  
print(result)

result = percentage(100, 20) 



print(result)

print('this is a demo for empire')



result = square_number(5)  
print(result)

result = cube_number(3)
print(result)

print('this is a demo for empire 4')