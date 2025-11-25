# 11/25/2025

# Conditionals exercise: simple login system with username and password checks

# Stored correct credentials
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "1234"

# Ask user for their credentials
username = input("Enter username ").lower()
password = input("Enter password ").lower()

def login(username, password):
    """Return login result based on username and password checks."""
 
    # Check if username is correct    
    if username == CORRECT_USERNAME:

        # Check if username is correct; now check password
        if password == CORRECT_USERNAME:
            return "The login was correct"
        else:
            return "The password was incorrect"
        # If username is incorrect
    else:
        return "The username was incorrect"

# Display the login result
print(login(username, password))