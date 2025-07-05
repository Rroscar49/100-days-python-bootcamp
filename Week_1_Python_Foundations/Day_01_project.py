# Day 1 Project - Code goes here
# Simple Calculator

# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get user input for operation
operation = input("Choose operation (+, -, *, /): ")

# Calculate result based on operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

# Print the result
print("Result:", result)

# End of Day 1 Project
# Note: This is a simple calculator that performs basic arithmetic operations.
# It does not handle complex expressions or error checking beyond division by zero.