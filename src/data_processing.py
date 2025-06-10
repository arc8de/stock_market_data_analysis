import pandas as pd
import numpy as np
import yfinance as yf

def fetch_stock_data(tickers, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance
    """
    data = yf.download(tickers, start=start_date, end=end_date)
    data = data.stack(level=1).rename_axis(['Date', 'Ticker']).reset_index()
    return data

def calculate_technical_indicators(df):
    """
    Calculate technical indicators for stock data
    """
    # Calculate returns
    df['Daily_Return'] = df.groupby('Ticker')['Close'].pct_change()
    
    # Moving Averages
    df['MA_20'] = df.groupby('Ticker')['Close'].rolling(window=20).mean().reset_index(0, drop=True)
    df['MA_50'] = df.groupby('Ticker')['Close'].rolling(window=50).mean().reset_index(0, drop=True)
    
    # RSI
    for ticker in df['Ticker'].unique():
        delta = df[df['Ticker'] == ticker]['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        df.loc[df['Ticker'] == ticker, 'RSI'] = rsi
    
    return df

def preprocess_data(df):
    """
    Data cleaning and preprocessing
    """
    # Handle missing values
    df = df.dropna()
    
    # Add sector information
    sectors = pd.read_csv('data/sectors.csv')
    df = pd.merge(df, sectors, on='Ticker')
    
    # Calculate volatility
    df['Volatility'] = df.groupby('Ticker')['Daily_Return'].transform(lambda x: x.rolling(30).std())
    
#     return df
# def preprocess_data(df):
#     # Merge sector info
#     sectors_csv_path = 'data/sectors.csv'  # Define the path to your sectors CSV file
#     sectors = pd.read_csv(sectors_csv_path)
#     df = pd.merge(df, sectors, on='Ticker')

#     # Calculate daily return
#     df['Daily_Return'] = df.groupby('Ticker')['Adj Close'].pct_change()

#     # Calculate volatility
#     df['Volatility'] = df.groupby('Ticker')['Daily_Return'].transform(lambda x: x.rolling(30).std())

#     return df
