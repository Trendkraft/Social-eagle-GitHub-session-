import streamlit as st

st.title("🔤 Vowel Counter")

# Input text
word = st.text_input("Enter a word:")

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
if word:
    count = sum(1 for char in word if char in vowels)
    st.success(f"✅ The word **'{word}'** contains **{count}** vowel(s).")


