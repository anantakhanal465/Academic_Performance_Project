
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title("Data Overview")
    df = pd.read_csv("data/academic_cleaned.csv")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Correlation Heatmap")
    numeric_df = df.select_dtypes(include='number')
    fig, ax = plt.subplots()
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

if __name__ == "__main__":
    app()
