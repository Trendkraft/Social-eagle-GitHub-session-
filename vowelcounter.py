# Program to count vowels in a given word

# Input from user
word = input("Enter a word: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize count
count = 0

# Loop through each character in the word
for char in word:
    if char in vowels:
        count += 1

# Output result
print(f"Number of vowels in '{word}' is: {count}")
