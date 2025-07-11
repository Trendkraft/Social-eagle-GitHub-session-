import streamlit as st

st.title("📊 Welcome to the Number Analyzer")

# Ask for user's name
name = st.text_input("👤 Enter your name:")

# Ask for list of numbers
input_text = st.text_area("🔢 Enter exactly 50 numbers (separated by commas or spaces):")

# Function to parse numbers safely
def parse_numbers(text):
    try:
        # Support comma or space separated input
        raw_parts = text.replace(",", " ").split()
        numbers = [int(num) for num in raw_parts]
        return numbers
    except ValueError:
        return None

# Button to trigger analysis
if st.button("Analyze"):
    if not name:
        st.error("❌ Please enter your name.")
    else:
        numbers = parse_numbers(input_text)

        if numbers is None:
            st.error("❌ Invalid input. Please enter only numbers.")
        elif len(numbers) != 50:
            st.warning(f"⚠️ You entered {len(numbers)} numbers. Please enter exactly 50.")
        else:
            # Count positives, negatives, and zeros
            positives = sum(1 for n in numbers if n > 0)
            negatives = sum(1 for n in numbers if n < 0)
            zeros = sum(1 for n in numbers if n == 0)

            st.success(f"✅ Hi {name}, here is your analysis:")
            st.write(f"🟢 Positive numbers: **{positives}**")
            st.write(f"🔴 Negative numbers: **{negatives}**")
            st.write(f"🟡 Zeros: **{zeros}**")

