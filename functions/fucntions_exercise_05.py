# 11/22/2025

#  Function that calculates 3 parameters

def calculate_total(price, quantity, tax_rate = 0.07):
    """Return the final cost after applying tax to subtotal."""
    sub_total = price * quantity                # Price before tax
    tax_amount = sub_total * tax_rate           # Tax added
    final_total = sub_total + tax_amount        # Total after tax
    return final_total

# Calculate totals using default and custom tax rates
total_default = calculate_total(10, 3)          # Uses 7% tax rate
total_custom = calculate_total(10, 3, 0.08)     # Uses 8% tax rate

# Display the results
print(total_default)
print(total_custom)