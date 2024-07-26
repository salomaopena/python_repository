# Import necessary libraries
import yfinance as yf
import pandas as pd
import streamlit as st

data = yf.Ticker("AMZN")

# Get historical market data
data_news = pd.DataFrame(data.news)
st.dataframe(data_news)
data_hist = data.history(period=max,start='2023-07-26', end='2024-07-26',interval='5d')


print(data_news)

   

