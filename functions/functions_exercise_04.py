# 11/22/25

# Functions exercise: return True if number is even, False if number is odd

# Ask user for number
user_number = int(input("Please enter your number "))

def is_even(user_number):
    if user_number % 2 == 0:
        return True
    else:
        return False
    
# Call the function and return the result
result = is_even(user_number)

# Display the result
print(f"You selected {user_number}. That number is {result}.")
