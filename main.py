import yfinance as yf
import streamlit as st
import pandas as pd

#st.write("""
# Tech Stock Price Tracking App 

#Here are the ***FAANG*** **Closing** stock prices and their **Volumes** repectively!

#""")

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

tickerDfF = tickerDataFB.history(period='1d', start='2005-12-25', end='2021-12-25')
# Open High  Low Close  Volume Dividends  Stock Splits
tickerDfA = tickerDataAMZN.history(period='1d', start='2005-12-25', end='2021-12-25')
# Open High  Low Close  Volume Dividends  Stock Splits
tickerDfA2 = tickerDataAAPL.history(period='1d', start='2005-12-25', end='2021-12-25')
# Open High  Low Close  Volume Dividends  Stock Splits
tickerDfN = tickerDataNFLX.history(period='1d', start='2005-12-25', end='2021-12-25')
# Open High  Low Close  Volume Dividends  Stock Splits
tickerDfG = tickerDataGOOG.history(period='1d', start='2005-12-25', end='2021-12-25')
# Open High  Low Close  Volume Dividends  Stock Splits
tickerDfT = tickerDataTSLA.history(period='1d', start='2005-12-25', end='2021-12-25')
# Open High  Low Close  Volume Dividends  Stock Splits


st.write("# :rocket: The ***FAANG*** Stock Spotlight :rocket: ")
st.write("From Christmas 2005-2021")
st.write("# ***F***:")
st.write("## Facebook Closing Stock Price History")
st.line_chart(tickerDfF.Close)
st.write("## Facebook Volume history ")
st.line_chart(tickerDfF.Volume)
st.write("# ***A***:")
st.write("## Amazon Closing Stock Price History,")
st.line_chart(tickerDfA.Close)
st.write("## Amazon Volume history ")
st.line_chart(tickerDfA.Volume)
st.write("# ***A***:")
st.write("## Apple Closing Stock Price History,")
st.line_chart(tickerDfA2.Close)
st.write("## Apple Volume history ")
st.line_chart(tickerDfA2.Volume)
st.write("# ***N***:")
st.write("## Netflix Closing Stock History,")
st.line_chart(tickerDfN.Close)
st.write("## Netflix Volume history ")
st.line_chart(tickerDfN.Volume)
st.write("# ***G***:")
st.write("## Google Closing Stock Price History,")
st.line_chart(tickerDfG.Close)
st.write("## Google Volume history ")
st.line_chart(tickerDfG.Volume)
st.write("## -------------------------------------------")
st.write("# This is the whole ***FAANG*** Stock Closing/Volume Portfolio")
st.write("## -------------------------------------------")
st.write("Here is a bonus Tesla Tracker")

st.write("## Tesla Closing Stock Price History,",
"It's not ***FAANG*** but :rocket:s are cool! ")
st.line_chart(tickerDfT.Close)
st.write("## Tesla Volume history ")
st.line_chart(tickerDfT.Volume)