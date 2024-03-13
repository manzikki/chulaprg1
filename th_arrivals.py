#Written by marko.n@chula.ac.th (actually ChatGPT)
#please install: 
# pip3 install streamlit pandas matplotlib
#then run:
#python3 -m streamlit run th_arrivals.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Reading data from CSV file
df = pd.read_csv('th_arrivals.csv')

# Streamlit app
st.title('Tourist Arrivals (in millions)')

# Creating the bar chart
fig, ax = plt.subplots()
ax.bar(df['Year'], df['Arrivals'], color='skyblue')
ax.set_xlabel('Year')
ax.set_ylabel('Arrivals (in millions)')
ax.set_title('Tourist Arrivals from 2006 to 2023')

# Set x-axis to display each year as integer
ax.set_xticks(df['Year'])  # Set x-ticks to be the years
ax.set_xticklabels(df['Year'], rotation=45)  # Set x-tick labels to be the years, rotated for better visibility

st.pyplot(fig)

