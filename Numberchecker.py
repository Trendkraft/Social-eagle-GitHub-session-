def is_positive(number):
    return number > 0

def is_even(number):
    return number % 2 == 0

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

# --- Main Execution ---
if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"Positive: {is_positive(num)}")
        print(f"Even: {is_even(num)}")
        print(f"Prime: {is_prime(num)}")
    except ValueError:
        print("Please enter a valid integer.")
