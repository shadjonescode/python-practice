# 11/21/2025

# Ask the user for the weather temperature in Celsius and store as a string
celsius_temp = input("What is the temperature in Celsius? ")

# Convert the input to an integer and apply the Celsius-to-Fahrenheit formula
fahrenheit_temp = (int(celsius_temp) * 9/5) + 32

# Print the Fahrenheit temperature in readable format using f-string
print(f"The temperature in Fahrenheit is {fahrenheit_temp} \u00B0F")