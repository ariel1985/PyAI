"""
Script shows a basic calculator

"""

print('\n\nPlease enter 2 numbers and get the results for:\n\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division')

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print('\nFor numbers: ', num1, num2)
print('1. Addition', num1 + num2)
print('2. Subtraction', num1 - num2)
print('3. Multiplication', num1 * num2)
print('4. Division', num1 / num2)