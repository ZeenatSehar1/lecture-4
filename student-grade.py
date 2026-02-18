import streamlit as st
import pandas as pd

# Initialize session state for storing students
if "students" not in st.session_state:
    st.session_state.students = []

st.set_page_config(page_title="Student Grade System", page_icon="🎓", layout="centered")

st.title("🎓 Student Grade System")
st.markdown("Enter student names and scores to calculate average, highest, lowest, total students, and grades.")

# Student input form
with st.form(key="student_form"):
    col1, col2 = st.columns([2,1])
    with col1:
        name = st.text_input("Student Name")
    with col2:
        score = st.number_input("Score", min_value=0.0, max_value=100.0, step=1.0)

    submitted = st.form_submit_button("Add Student")
    
    if submitted:
        if name.strip() == "":
            st.warning("Please enter a name!")
        else:
            st.session_state.students.append({"Name": name.strip(), "Score": score})
            st.success(f"Added {name} with score {score}.")

# Display students and grades
if st.session_state.students:
    st.subheader("📋 Student Scores & Grades")

    # Create DataFrame
    df = pd.DataFrame(st.session_state.students)
    
    # Assign grades
    def assign_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    df["Grade"] = df["Score"].apply(assign_grade)

    st.table(df)

    # Statistics
    scores = df["Score"]
    st.subheader("📊 Summary")
    st.markdown(f"**Average Score:** {scores.mean():.2f}  ")
    st.markdown(f"**Highest Score:** {scores.max()}  ")
    st.markdown(f"**Lowest Score:** {scores.min()}  ")
    st.markdown(f"**Total Students:** {len(df)}  ")

# Clear all students button
if st.session_state.students:
    if st.button("🗑️ Clear All Students"):
        st.session_state.students = []
        st.success("All students cleared.")
