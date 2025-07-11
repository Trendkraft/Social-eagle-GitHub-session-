# Function to determine age group
def age_group(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif 20 <= age <= 59:
        return "Adult"
    else:
        return "Senior"

# Ask user for input
try:
    age_input = int(input("Enter your age: "))
    category = age_group(age_input)
    print(f"You are classified as: {category}")
except ValueError:
    print("Please enter a valid number.")
