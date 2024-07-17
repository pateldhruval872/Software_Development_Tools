import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Header
st.header('Car Advertisement Analysis')

# Histogram
fig_price_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_price_hist)

# Scatter plot
fig_price_model_year = px.scatter(df, x='model_year', y='price', title='Price vs. Model Year')
st.plotly_chart(fig_price_model_year)

# Checkbox to show/hide the scatter plot
if st.checkbox('Show Scatter Plot'):
    st.plotly_chart(fig_price_model_year)
