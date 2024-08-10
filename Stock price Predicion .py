# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 18:44:06 2024

@author: balak
"""

import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write(
    """
    # Stock Price Analyser
    
    """
    )


ticker_symbol= st.text_input(
    "Enter Stock Symbol",
    "AAPL",
    key="placeholder"
    )
#ticker_symbol="AAPL"
col1, col2 = st.columns(2)

with col1:
    start_date=st.date_input("Input Starting Date",
              datetime.date(2019,1,1))
with col2:
    end_date=st.date_input("Input ending Date",
                  datetime.date(2022,12,31))

ticker_data=yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period="1d",
                              start=f"{start_date}",
                              end=f"{end_date}")
st.write(f"""
         ### {ticker_symbol}'s EOD prices
         """
         )
st.dataframe(ticker_df)
st.write(
    """
    ## Daily Closing Price Data
    
    """)
st.line_chart(ticker_df.Close)

st.write(
    """
    ## volume of shares
    
    """)
st.line_chart(ticker_df.Volume)
