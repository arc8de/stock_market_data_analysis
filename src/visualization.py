import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf
import plotly.express as px

def plot_candlestick(df, ticker):
    """
    Plot interactive candlestick chart with Plotly
    """
    stock_df = df[df['Ticker'] == ticker]
    fig = px.line(stock_df, x='Date', y='Close', title=f'{ticker} Closing Price')
    fig.show()

def plot_sector_performance(df):
    """
    Plot sector-wise performance using Plotly
    """
    sector_perf = df.groupby('Sector')['Daily_Return'].mean().reset_index()
    fig = px.bar(sector_perf, x='Sector', y='Daily_Return', 
                 title='Average Daily Returns by Sector')
    fig.show()

def plot_correlation_heatmap(df):
    """
    Plot correlation matrix between stocks
    """
    pivot_df = df.pivot(index='Date', columns='Ticker', values='Close')
    returns_df = pivot_df.pct_change().corr()
    
    plt.figure(figsize=(12,8))
    sns.heatmap(returns_df, annot=True, cmap='coolwarm')
    plt.title('Stock Correlation Matrix')
    plt.show()