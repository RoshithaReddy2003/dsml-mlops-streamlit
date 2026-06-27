import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

st.title('stock market app')
st.write('This is hope of my getting hike!!!')

tickter_symbol = st.text_input("Enter the stock ticker symbol (e.g., AAPL, MSFT, GOOGL):", "AAPL")

ticker_data=yf.Ticker(tickter_symbol)

hist=ticker_data.history(start=st.text_input('Enter the start date (YYYY-MM-DD):', '2020-01-01'), 
                         end=st.text_input('Enter the end date (YYYY-MM-DD):', '2022-01-01'))

st.write('I am going to show you the stock data of Apple')
#st.write(hist)
st.dataframe(hist)

# st.write("This plot is for volume of the stock")
# st.line_chart(hist.Volume)


# import streamlit as st

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg")


col1, col2 = st.columns(2)
with col1:
    st.write("This plot is for volume of the stock")
    st.line_chart(hist.Volume)

with col2:
    st.write("This plot is for price of the stock")
    st.line_chart(hist.Close)