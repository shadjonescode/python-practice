# 11/22/2025
# Functions exercise: compute the average of three numbers
# Using NumPy to practice working with external libraries

import numpy as np

def average_num(num1, num2, num3):
    """Return the average of three numbers using NumPy."""
    numbers = np.array([num1, num2, num3])  # Create array of the inputs
    average = np.mean(numbers)              # Compute the mean using NumPy
    return average

# Example numbers
num1 = 2
num2 = 23
num3 = 74

# Call the function and display the result
avg_result = average_num(num1, num2, num3)
print(f"The average of {num1}, {num2}, {num3} is: {avg_result}")
