# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even"
    else:
        return f"{num} is Odd"

# 1. Check a single number
number = int(input("Enter a number to check even or odd: "))
print(check_even_odd(number))

# 2. Check a list of numbers
print("\nNow checking a list of numbers...")

# Example list (you can change this)
number_list = [10, 3, 7, 8, 12, 5, 19]

for n in number_list:
    print(check_even_odd(n))
