# Python calculator

operator = input("Enter an operator (+, -, *, /) for arithmatic operation: ")

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {round(result, 2)}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {round(result, 2)}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {round(result, 2)}")
elif operator == "+":
    result = num1 / num2
    print(f"{num1} / {num2} = {round(result, 2)}")
else:
    print(f"{operator} is an invalid operator")