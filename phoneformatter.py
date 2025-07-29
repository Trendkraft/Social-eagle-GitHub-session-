def format_phone_number(number):
    # Ensure the number is a string and has exactly 10 digits
    number = str(number)
    if len(number) != 10 or not number.isdigit():
        return "Invalid input! Please enter a 10-digit number."

    # Format the number
    formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
    return formatted

# Main program
if __name__ == "__main__":
    user_input = input("Enter a 10-digit phone number: ")
    result = format_phone_number(user_input)
    print("Formatted Number:", result)
