num1 = float(input("Enter First Number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter Second Number: "))


def calculate(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        return "Invalid Operator"


print(calculate(num1, op, num2))
