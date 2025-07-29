def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birth_year, current_year):
    """Calculate age from birth year and current year."""
    return current_year - birth_year

# Main program
if __name__ == "__main__":
    year = int(input("Enter a year to check if it's a leap year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

    birth_year = int(input("Enter your birth year: "))
    current_year = int(input("Enter the current year: "))

    age = calculate_age(birth_year, current_year)
    print(f"Your age is: {age}")
