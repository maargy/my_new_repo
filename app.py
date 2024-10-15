import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

df = pd.read_csv('vehicles_us.csv')

st.title('Data Analysis with Car Prices: Exploring Trends and Insights')

#Histogram of 'Average Price by Model Year'
avg_price_year = df.groupby('model_year')['price'].mean().reset_index()
avg_price_year = avg_price_year[avg_price_year['model_year'] >= 1908]  # to not include 0

hist = px.histogram(avg_price_year, x='model_year', y='price', title='Average Price by Model Year')
hist.update_xaxes(title='Model Year')
hist.update_yaxes(title='Average Price')

st.plotly_chart(hist)

# Creating a checkbox
show_graph = st.checkbox("Show Price vs. Odometer Graph")

#Scatterplot of Price vs. Odometer
if show_graph:
    scat = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer', 
                     labels={'odometer': 'Odometer (miles)', 'price': 'Price'})
    scat.update_traces(marker=dict(size=5, opacity=0.5))

st.plotly_chart(scat)

