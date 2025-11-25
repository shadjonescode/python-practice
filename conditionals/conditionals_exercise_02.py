# 11/25/2025

# Conditionals exercise: Ask user for number and determine if it's high, medium, or low

# Ask user for number

number = int(input("Please enter a number between 1-100 "))

def high_medium_low(number):
    """Return whether the number is high, medium, or low."""

    # low range
    if number < 30:
        return "Your number is low"
    
    # Medium range
    elif 30 <= number <= 70:
        return "Your number is medium"
    
    # High range
    else:
        return "Your number is high"
    
    # Display classification
print(high_medium_low(number))