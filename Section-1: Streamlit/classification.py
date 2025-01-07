import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Caches the function's output to avoid reloading the dataset every time the app reruns.


@st.cache_data
def load_data():
    # Loads the Iris dataset, which contains measurements of iris flowers and their species.
    dataset = load_iris()
    # Converts the dataset into a DataFrame for easier manipulation.
    df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    # A new column, species, is added to the DataFrame, storing the target (species labels as integers: 0, 1, 2).
    df['species'] = dataset.target
    # df:A DataFrame with the iris data and species labels.
    # dataset.target_names: An array of species names (['setosa', 'versicolor', 'virginica']).
    return df, dataset.target_names


# The data is loaded
df, target_names = load_data()
# A RandomForestClassifier is instantiated and trained
model = RandomForestClassifier()
# Features: All columns except the last (iloc[:, :-1]).
# Target: The species column (df['species']).
# This model learns how to classify iris species based on the provided features.
model.fit(df.iloc[:, :-1], df['species'])

# A sidebar is created with sliders for each feature of the iris flower
st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal length", float(
    df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal width", float(
    df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length", float(
    df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width", float(
    df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

# A list containing the user-inputted feature values.
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

#  Predicts the species based on the user inputs.
prediction = model.predict(input_data)
# Converts the numeric prediction into the corresponding species name.
predicted_species = target_names[prediction[0]]

# Displays the prediction result in the main area of the app
st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")
