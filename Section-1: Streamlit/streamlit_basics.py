import streamlit as st
import pandas as pd
import numpy as np

# Application title
st.title("This is a title")

# Display simple text
st.write("Hello, Streamlit")

# Create a simple dataframe
df = pd.DataFrame({
    "First Column:": [1, 2, 3, 4, 5],
    "Second Column:": [10, 20, 30, 40, 50]
}
)

# Display the dataframe
st.write("Here's the dataframe")
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)
