from art import logo

print(logo)

# Calculator --> Add, Subtract, Multiply, Divide


# Add
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


num1 = float(input("Type the first operand:\n"))
num2 = float(input("Type the second operand:\n"))

for operation in operations:
    print(operation)

operation_symbol = input("Please choose the operation from the line above:\n")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")