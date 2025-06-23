import streamlit as st
from app import Home, Academic_Prediction  # removed Data_Overview

# Sidebar for navigation
st.sidebar.title("📚 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Predict"])  # removed "Data Overview"

# Render selected page
if page == "Home":
    Home.app()
elif page == "Predict":
    Academic_Prediction.app()
