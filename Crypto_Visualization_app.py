import yfinance as yf
import streamlit as st
from datetime import datetime, timedelta
import plotly.graph_objects as go

# Function to fetch historical cryptocurrency data
def get_crypto_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data[['Open', 'High', 'Low', 'Close']]

# title
st.title(":orange[Crypto Currency Visualization App]")

# Sidebar for user input
st.sidebar.header(':blue[Input Values]', divider='rainbow')

# Select cryptocurrency
#crypto_symbol = st.sidebar.text_input('Enter Cryptocurrency Symbol (e.g., BTC-USD):', 'BTC-USD')


# Get a list of available cryptocurrency symbols
crypto_symbols = [
    'BTC-USD', 'ETH-USD', 'LTC-USD', 'XRP-USD', 'BCH-USD', 'ADA-USD',
    'DOT-USD', 'LINK-USD', 'XLM-USD', 'USDT-USD', 'BNB-USD', 'DOGE-USD',
    'UNI-USD', 'USDC-USD', 'EOS-USD', 'TRX-USD', 'XMR-USD', 'XTZ-USD',
    'ATOM-USD', 'VET-USD', 'DASH-USD', 'MIOTA-USD', 'NEO-USD', 'MKR-USD'
]

# Select cryptocurrency using a dropdown menu
crypto_symbol = st.sidebar.selectbox('Select Cryptocurrency :', crypto_symbols, index=0)


# Select date range
# Calculate the default start date as one month before today's date
start_date_default = datetime.now() - timedelta(days=30)

# Set the default start date to one day before today's date
start_date = st.sidebar.date_input('Start Date', value=start_date_default)

# Set the default end date to today's date
end_date = st.sidebar.date_input('End Date', value=datetime.now())

# Fetch data

crypto_data = get_crypto_data(crypto_symbol, start_date, end_date)

# Allow user to pick the number of rows to display
num_rows = st.sidebar.slider('Select the number of rows to display:', min_value=1, max_value=len(crypto_data), value=5)

# Display the selected number of rows
#st.write(f'**:green[{crypto_symbol} Historical Data (OHLC) (Top {num_rows} rows)]**')
#st.write(crypto_data.tail(num_rows)).
# Display the selected number of rows in descending order
st.write(f'**:green[{crypto_symbol} Historical Data (OHLC) (Top {num_rows} rows)]**')
st.write(crypto_data.sort_index(ascending=False).head(num_rows))


# Line chart with all values (Open, High, Low, Close)
#st.write(f'**:green[{crypto_symbol} OHLC Prices Over Time]**')
line_chart_ohlc = go.Figure()

line_chart_ohlc.add_trace(go.Scatter(x=crypto_data.index, y=crypto_data['Open'], mode='lines', name='Open'))
line_chart_ohlc.add_trace(go.Scatter(x=crypto_data.index, y=crypto_data['High'], mode='lines', name='High'))
line_chart_ohlc.add_trace(go.Scatter(x=crypto_data.index, y=crypto_data['Low'], mode='lines', name='Low'))
line_chart_ohlc.add_trace(go.Scatter(x=crypto_data.index, y=crypto_data['Close'], mode='lines', name='Close'))

line_chart_ohlc.update_layout( xaxis_title='Date',
                              yaxis_title='Price (USD)',
                              title=dict(text=f'{crypto_symbol} OHLC Prices Over Time', font=dict(color='green')),)

st.plotly_chart(line_chart_ohlc)


# Candlestick chart
#st.write(f'**:green[{crypto_symbol} Candlestick Chart]**')

candlestick_chart = go.Figure(data=[go.Candlestick(x=crypto_data.index,
                                                    open=crypto_data['Open'],
                                                    high=crypto_data['High'],
                                                    low=crypto_data['Low'],
                                                    close=crypto_data['Close'])])

candlestick_chart.update_layout(xaxis_title='Date', yaxis_title='Price (USD)',
                                title=dict(text=f'{crypto_symbol} OHLC Prices Over Time', font=dict(color='green')),)

st.plotly_chart(candlestick_chart)
