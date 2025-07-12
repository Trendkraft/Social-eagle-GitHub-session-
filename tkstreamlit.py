import streamlit as st

st.title("➕ Sum of Numbers from 1 to N")

# Input from the user
n = st.number_input("Enter a positive integer (N):", min_value=1, step=1)

# Calculate sum using a loop
total = 0
for i in range(1, n + 1):
    total += i

# Display the result
st.write(f"The sum of numbers from 1 to {int(n)} is: **{total}**")



