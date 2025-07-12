# Basic Password Validator

def is_valid_password(password, min_length=8):
    if len(password) < min_length:
        return False, f"❌ Password must be at least {min_length} characters long."
    else:
        return True, "✅ Password is valid!"

# Input from user
password = input("Enter your password: ")
valid, message = is_valid_password(password)
print(message)
