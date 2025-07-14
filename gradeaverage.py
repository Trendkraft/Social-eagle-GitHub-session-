import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Academic Performance Dashboard")

# Subject list
subjects = ["Tamil", "English", "Maths", "Science", "Social"]

# Store student data
students = []

# Get 5 student entries
for i in range(1, 6):
    st.subheader(f"👨‍🎓 Student {i}")
    name = st.text_input(f"Name of Student {i}", key=f"name_{i}")
    marks = []
    for subject in subjects:
        mark = st.number_input(f"{subject} Marks", min_value=0, max_value=100, key=f"{subject}_{i}")
        marks.append(mark)
    
    if name:
        total = sum(marks)
        average = total / len(subjects)
        result = "✅ Pass" if average >= 40 else "❌ Fail"
        students.append({
            "Name": name,
            "Total": total,
            "Average": average,
            "Result": result,
            **{subjects[j]: marks[j] for j in range(len(subjects))}
        })

# Show report only if all students are entered
if len(students) == 5:
    df = pd.DataFrame(students)

    st.subheader("📋 Student Report")
    st.dataframe(df)

    # To
