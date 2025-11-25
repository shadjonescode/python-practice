# 11/22/2025

# Conditionals exercise: determine if user is an adult or minor

# Ask the user for their age
age = int(input("Please enter your age "))

def adult_or_minor(age):
    """Return whether the user is an adult or minor."""
    if age >= 18:
        return "You are an adult" 
    else:
        return "You are a minor"
    
# Call the function and display the result
print(adult_or_minor(age))