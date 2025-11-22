# 11/22/2025

# Functions exercise: greet user using input and an f-string

# Ask user for their name

name = input("Please enter your name ")

def greet(name):
    """Return the users input information then using it in a f-string"""
    return f"Hello, {name}! How are you doing?"


# Call the function and print the greeting
print(greet(name))