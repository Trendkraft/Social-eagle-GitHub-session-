# Function to calculate total with tax
def calculate_total_with_tax(prices, tax_percent):
    subtotal = sum(prices)
    tax = (tax_percent / 100) * subtotal
    total = subtotal + tax
    return subtotal, tax, total

# Input for 3 items
try:
    item1 = float(input("Enter price of item 1: ₹"))
    item2 = float(input("Enter price of item 2: ₹"))
    item3 = float(input("Enter price of item 3: ₹"))
    tax_percent = float(input("Enter tax percentage: "))

    # Calculate
    prices = [item1, item2, item3]
    subtotal, tax, total = calculate_total_with_tax(prices, tax_percent)

    # Output
    print(f"\nSubtotal: ₹{subtotal:.2f}")
    print(f"Tax (@{tax_percent}%): ₹{tax:.2f}")
    print(f"Total Amount: ₹{total:.2f}")

except ValueError:
    print("❌ Invalid input. Please enter numbers only.")
