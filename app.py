import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')


# Header
st.title('Car Advertisement Analysis')
st.write("""
    This analysis aims to explore the dataset of car advertisements in the United States. 
    We will perform exploratory data analysis (EDA) to understand the distribution of car prices, 
    and the relationship between the model year and car prices.
""")

# Histogram of car prices
st.header('Price Distribution')
fig_price_hist = px.histogram(df, x='price', title='Price Distribution')
fig_price_hist.update_layout(xaxis_title='Price', yaxis_title='Count')
st.plotly_chart(fig_price_hist)
st.write("The histogram shows the distribution of car prices. We can observe that most car prices are concentrated at the lower end, indicating that the majority of cars are relatively inexpensive.")

# Scatter plot of price vs. model year
st.header('Price vs. Model Year')
fig_price_model_year = px.scatter(
    df, x='model_year', y='price', title='Price vs. Model Year')
fig_price_model_year.update_layout(
    xaxis_title='Model Year', yaxis_title='Price')
st.plotly_chart(fig_price_model_year)
st.write("The scatter plot illustrates the relationship between car prices and model years. It shows that newer car models tend to have higher prices, as expected.")

# Filter to exclude expensive vehicles
max_price = st.slider('Select the maximum price to include in the scatter plot:', min_value=int(
    df['price'].min()), max_value=int(df['price'].max()), value=int(df['price'].max()))
filtered_df = df[df['price'] <= max_price]

fig_filtered_price_model_year = px.scatter(
    filtered_df, x='model_year', y='price', title='Price vs. Model Year (Filtered)')
fig_filtered_price_model_year.update_layout(
    xaxis_title='Model Year', yaxis_title='Price')
st.plotly_chart(fig_filtered_price_model_year)
st.write(
    f"The scatter plot now excludes vehicles with prices higher than {max_price}. This helps us focus on the more common price range and avoid outliers.")

# Overall conclusion
st.header('Overall Conclusion')
st.write("""
    The analysis reveals that the majority of car advertisements are for relatively inexpensive vehicles. 
    There is a clear trend showing that newer car models are priced higher than older ones. 
    Filtering out the most expensive vehicles helps in better understanding the common price range in the dataset.
""")
