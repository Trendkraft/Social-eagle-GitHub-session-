import math

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    return math.factorial(n)

def calculate_power(base, exponent):
    return math.pow(base, exponent)

def calculate_square_root(x):
    if x < 0:
        return "Square root is not defined for negative numbers."
    return math.sqrt(x)

# --- Main Execution ---
if __name__ == "__main__":
    print("Math Operations\n")

    # Factorial
    number = int(input("Enter a number for factorial: "))
    print(f"Factorial of {number} = {calculate_factorial(number)}")

    # Power
    base = float(input("\nEnter base for power calculation: "))
    exponent = float(input("Enter exponent: "))
    print(f"{base} ^ {exponent} = {calculate_power(base, exponent)}")

    # Square Root
    x = float(input("\nEnter a number for square root: "))
    print(f"Square root of {x} = {calculate_square_root(x)}")
