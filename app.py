# Importing the libraries!
import streamlit as st
import numpy as np
import pandas as pd

# Displaying the dataset! 
st.title('This is my first app!')
st.write('This is a dataframe table')
dataframe = pd.read_csv("dataset.txt")
st.write(dataframe)

# Creating the line chart!
st.write('This is a line_chart.')
st.line_chart(dataframe)

# Creating a area chart!
st.write('This is a area_chart.')
st.area_chart(dataframe)

# Creating a bar chart!
st.write('This is a bar_chart.')
st.bar_chart(dataframe)