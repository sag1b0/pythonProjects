# Python Calculator Project

operator = input ("Enter the Operator (+ - * /): ")
num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the second Number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))

else:
    print(f"{operator} is not a valid operator")