import streamlit as st
import pandas as pd

# Title
st.title("Streamlit text input")

# Input
user_input = st.text_input("Enter your name:")
if user_input:
    st.write(f"Hello, {user_input}!")

# Slider
age = st.slider("Please select your age:", 0, 100, 18)
st.write("Your age is:", age)

# Dropdown
options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your fav lang:", options)
st.write("Your fav lang is:", choice)

# Print and save dataframe
data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

# Upload file
file = st.file_uploader("Please upload a csv", type='csv')
if file is not None:
    df = pd.read_csv(file)
    st.write(df)
