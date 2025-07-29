def capitalize_text(text):
    return text.upper()

def reverse_text(text):
    return text[::-1]

def count_characters(text):
    return len(text)

# --- Main Execution ---
if __name__ == "__main__":
    user_input = input("Enter some text: ")

    print(f"\nCapitalized: {capitalize_text(user_input)}")
    print(f"Reversed: {reverse_text(user_input)}")
    print(f"Character Count: {count_characters(user_input)}")
