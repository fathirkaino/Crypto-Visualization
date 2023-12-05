import yfinance as yf
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
#import appdirs as ad
#ad.user_cache_dir = lambda *args: "/tmp"

# Function to fetch historical cryptocurrency data
def get_crypto_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

# Function to create candlestick chart
def create_candlestick_chart(data):
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])

    fig.update_layout(title='Cryptocurrency Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Price',
                      xaxis_rangeslider_visible=True)

    return fig

# Streamlit app
def main():
    st.title('Cryptocurrency Data Visualization')

    # Sidebar for user input
    st.sidebar.header('User Input')

    # Select cryptocurrency
    crypto_symbol = st.sidebar.text_input('Enter Cryptocurrency Symbol (e.g., BTC-USD):', 'BTC-USD')

    # Select date range
    start_date = st.sidebar.date_input('Start Date', value=datetime(2022, 1, 1))
    end_date = st.sidebar.date_input('End Date', value=datetime(2023, 1, 1))

    # Fetch data
    crypto_data = get_crypto_data(crypto_symbol, start_date, end_date)

    # Display the data
    st.write('**Historical Cryptocurrency Data**')
    st.write(crypto_data.head())

    # Create and display candlestick chart
    st.write('**Candlestick Chart**')
    candlestick_chart = create_candlestick_chart(crypto_data)
    st.plotly_chart(candlestick_chart)

if __name__ == "__main__":
    main()
