# 11/21/2025

# Ask the user for two numbers, then perform basic arithmetic operations

# Get user input and convert to integers
x = int(input("Pick your first number: "))
y = int(input("Pick your second number: "))

# Perform arithmetic operations
sum_result = x + y                    # add the two numbers
difference_result = x - y             # subtract y from x
product_result = x * y                # multiply the two numbers
quotient_result = x / y               # divide x by y

# Print the results with labels for clarity
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")