import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Tech Stock Price Tracking App

Here are the ***FAANG*** **Closing** stock prices and their **Volumes** repectively!

""")

tickerSymbol_FB = 'FB'
tickerSymbol_AMZN = 'AMZN'
tickerSymbol_AAPL = 'AAPL'
tickerSymbol_NFLX = 'NFLX'
tickerSymbol_GOOG = 'GOOGL'

tickerSymbol_TSLA = 'TSLA'

tickerDataFB = yf.Ticker(tickerSymbol_FB)
tickerDataAMZN = yf.Ticker(tickerSymbol_AMZN)
tickerDataAAPL = yf.Ticker(tickerSymbol_AAPL)
tickerDataNFLX = yf.Ticker(tickerSymbol_NFLX)
tickerDataGOOG = yf.Ticker(tickerSymbol_GOOG)
tickerDataTSLA = yf.Ticker(tickerSymbol_TSLA)

tickerDfF = tickerDataFB.history(period='1w', start='2011-12-21', end='2021-12-28')
# Open High  Low Close  Volume Dividends  Stock Splits
tickerDfA = tickerDataAMZN.history(period='1w', start='2011-12-21', end='2021-12-28')
# Open High  Low Close  Volume Dividends  Stock Splits
tickerDfA2 = tickerDataAAPL.history(period='1w', start='2011-12-21', end='2021-12-28')
# Open High  Low Close  Volume Dividends  Stock Splits
tickerDfN = tickerDataNFLX.history(period='1w', start='2011-12-21', end='2021-12-28')
# Open High  Low Close  Volume Dividends  Stock Splits
tickerDfG = tickerDataGOOG.history(period='1w', start='2011-12-21', end='2021-12-28')
# Open High  Low Close  Volume Dividends  Stock Splits
tickerDfT = tickerDataTSLA.history(period='1w', start='2011-12-21', end='2021-12-28')
# Open High  Low Close  Volume Dividends  Stock Splits


st.write("# ---The ***FAANG*** Stock Spotlight---")
st.write("# ***F***:")
st.write("# Facebook Stock Price History,",
"Facebook Closing stock and Volume history ")
st.line_chart(tickerDfF.Close)
st.line_chart(tickerDfF.Volume)
st.write("# ***A***:")
st.write("# Amazon Stock Price History,",
"Amazon Closing prices, followed by the Volume")
st.line_chart(tickerDfA.Close)
st.line_chart(tickerDfA.Volume)
st.write("# ***A***:")
st.write("# Apple Stock Price History,",
"Showcasing the Apple Closing and Volume graphed")
st.line_chart(tickerDfA2.Close)
st.line_chart(tickerDfA2.Volume)
st.write("# ***N***:")
st.write("# Netflix Stock History,",
"Netflix Closing prices followed by the Volume")
st.line_chart(tickerDfN.Close)
st.line_chart(tickerDfN.Volume)
st.write("# ***G***:")
st.write("# Google Stock Price History,",
"The final FAANG stock on our list!")
st.line_chart(tickerDfG.Close)
st.line_chart(tickerDfG.Volume)
st.write("# -------------------------------------------")
st.write("# This is the whole ***FAANG*** Stock Closing/Volume Portfolio")
st.write("# -------------------------------------------")
st.write("Here is a bonus Tesla Tracker")

st.write("# Tesla Stock Price History,",
"It's not ***FAANG*** but still cool! ")
st.line_chart(tickerDfT.Close)
st.line_chart(tickerDfT.Volume)