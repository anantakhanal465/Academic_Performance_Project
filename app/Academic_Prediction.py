import streamlit as st
import pandas as pd
import numpy as np
import joblib

def app():
    st.title("Predict Academic Performance")

    age = st.slider("Age", 17, 30, 21)
    gender = st.selectbox("Gender", ["Male", "Female"])
    study_hours = st.slider("Study Hours/Day", 0.0, 12.0, 2.0)
    social_media = st.slider("Social Media Hours", 0.0, 10.0, 3.0)
    netflix = st.slider("Netflix Hours", 0.0, 10.0, 2.0)
    job = st.selectbox("Part-time Job", ["Yes", "No"])
    attendance = st.slider("Attendance %", 50.0, 100.0, 85.0)
    sleep = st.slider("Sleep Hours", 3.0, 10.0, 7.0)
    diet = st.selectbox("Diet Quality", ["Poor", "Fair", "Good"])
    exercise = st.slider("Exercise Frequency (per week)", 0, 7, 3)
    parental = st.selectbox("Parental Education", ["High School", "Bachelor", "Master"])
    internet = st.selectbox("Internet Quality", ["Poor", "Average", "Good"])
    mental = st.slider("Mental Health Rating (1-10)", 1, 10, 5)
    extra = st.selectbox("Extracurricular Activities", ["Yes", "No"])

    if st.button("Predict"):
        model = joblib.load("model/model.pkl")
        expected_cols = joblib.load("model/feature_names.pkl")

        data = {
            'age': age,
            'study_hours_per_day': study_hours,
            'social_media_hours': social_media,
            'netflix_hours': netflix,
            'attendance_percentage': attendance,
            'sleep_hours': sleep,
            'exercise_frequency': exercise,
            'mental_health_rating': mental,
            'gender_Male': 1 if gender == 'Male' else 0,
            'part_time_job_Yes': 1 if job == 'Yes' else 0,
            'diet_quality_Fair': 1 if diet == 'Fair' else 0,
            'diet_quality_Good': 1 if diet == 'Good' else 0,
            'parental_education_level_High School': 1 if parental == 'High School' else 0,
            'parental_education_level_Master': 1 if parental == 'Master' else 0,
            'internet_quality_Good': 1 if internet == 'Good' else 0,
            'internet_quality_Poor': 1 if internet == 'Poor' else 0,
            'extracurricular_participation_Yes': 1 if extra == 'Yes' else 0
        }

        X_input = pd.DataFrame([data])
        for col in expected_cols:
            if col not in X_input:
                X_input[col] = 0
        X_input = X_input[expected_cols]

        prediction = model.predict(X_input)[0]
        st.success(f"Predicted Performance: **{prediction}**")

if __name__ == "__main__":
    app()