# 11/26/2025

# Conditionals exercise: simple menu system where the user selects Start, Options, Exit

# Ask user for their menu choice
choice = int(input("Enter 1, 2, or 3: "))

def user_options(choice):
    """Return result of the users menu selection."""

    # Check each possible menu option
    if choice == 1:
        return "Game starting"
    elif choice == 2:
        return "Opening settings..."
    else:
        return "exiting program"
    
# Display the result of users choice
print(user_options(choice))