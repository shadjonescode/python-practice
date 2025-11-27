# 11/25/2025

# Conditionals exercise: stacking multiple conditionals to determine letter grade based off of percentage

# Ask user for grade percentage
grade_percent = int(input("Please enter grade percentage "))

def letter_grade(grade_percent):
    """Return letter grade based on numeric percent"""

    if grade_percent >= 90:
        return "A"
    elif grade_percent >= 80:
            return "B"
    elif grade_percent >= 70:
            return "C"
    elif grade_percent >= 60:
            return "D"
    else:
          return "F"
    
    # Display calculated letter grade
print(letter_grade(grade_percent))