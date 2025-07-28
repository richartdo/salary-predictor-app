import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("salary_model.pkl")

st.title("💼 Salary Predictor AI")

st.markdown("Enter your details:")

experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=3)
education = st.selectbox("Education Level", ["High School", "Bachelor’s", "Master’s", "PhD"])
job_title = st.selectbox("Job Title", ["Software Engineer", "Data Scientist", "Analyst", "Project Manager"])
age = st.slider("Age", 18, 65, 25)

# Map categorical inputs (must match your training encoding!)
education_map = {"High School": 0, "Bachelor’s": 1, "Master’s": 2, "PhD": 3}
job_map = {"Software Engineer": 0, "Data Scientist": 1, "Analyst": 2, "Project Manager": 3}

education_encoded = education_map[education]
job_encoded = job_map[job_title]

# Input features as a list
features = np.array([[experience, education_encoded, job_encoded, age]])

# Predict and show result
if st.button("Predict Salary"):
    predicted_salary = model.predict(features)[0]
    st.success(f"Estimated Salary: ${int(predicted_salary):,}")
