# quick_calculator.py - Function-based single-line calculator

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: Invalid input ({e})"

print("=== Quick Calculator ===")
print("Enter a calculation (e.g., 10 + 5 or 8 * 2)")
print("Type 'exit' to quit")

while True:
    user_input = input("\nYour expression: ")

    if user_input.lower() == 'exit':
        print("Goodbye! 👋")
        break

    output = calculate(user_input)

    print("Result:", output)
    close
    
