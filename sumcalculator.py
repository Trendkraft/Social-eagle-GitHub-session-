# Find the sum of all numbers from 1 to n using a loop

# Input from user
n = int(input("Enter a positive integer: "))

# Initialize sum
total = 0

# Loop from 1 to n (inclusive)
for i in range(1, n + 1):
    total += i

# Display the result
print(f"The sum of numbers from 1 to {n} is: {total}")
