# Stock Market Analysis Project

## Overview
This project analyzes historical stock market data to identify trends, correlations, and predict future prices.

## Project Structure
```
📦 
├─ OUTPUT IMAGES
│  ├─ 2. AAPL CLOSING PRICE.png
│  ├─ 2. AAPL price with moving averages.png
│  ├─ 2. Average Daily Returns by Sector.png
│  ├─ 2. Stock Correlation matrix.png
│  └─ 3 .Final AAPL Price Forecast.png
├─ README.md
├─ notebooks
│  ├─ 1. Stock Data Cleaning.ipynb
│  ├─ 2. Exploratory Data Analysis.ipynb
│  ├─ 3. Predictive Modeling.ipynb
│  └─ data
│     ├─ sectors.csv
│     └─ stock_data.csv
├─ requirements.txt
└─ src
   ├─ data_processing.py
   └─ visualization.py
```

## Setup
1. Clone the repository
2. Install requirements: `pip install -r requirements.txt` or install it one by one from txt file
3. Run notebooks in order:
   - 1. `1. Stock Data Cleaning.ipynb` (Fetches live data)
   - 2. `2. Exploratory Data Analysis.ipynb`
   - 3. `3. Predictive Modeling.ipynb`

**Note:** The files above contain example output for only selected ticker symbol. If users wish, they can update the ticker symbol in `notebooks/2. Exploratory Data Analysis.ipynb` and `notebooks/3. Predictive Modeling.ipynb` that are present in `notebooks/1. Stock Data Cleaning.ipynb` accordingly for other outputs.

## Changing the Analyzed Stocks

To analyze stock data for different companies:

1. Open `notebooks/1. Stock Data Cleaning.ipynb`.
2. Locate the following code cell:
   ```python
   tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 
              'JPM', 'GS', 'WMT', 'NVDA', 'NFLX']
   ```
3. Replace the ticker symbols in the `tickers` list with the symbols of the companies you want to analyze (e.g., `['META', 'TTM', ...]`).
4. Run all cells in the notebook to download and clean the new data.
5. The other notebooks (`2. Exploratory Data Analysis.ipynb` and `3. Predictive Modeling.ipynb`) will automatically use the updated data.

**Note:** You can find ticker symbols for companies on Yahoo Finance or Google Finance.

## Features
- Live data fetching from Yahoo Finance
- Technical indicator calculation
- Interactive visualizations
- Price forecasting with Prophet
- Sector performance analysis

## Sample Outputs
- Candlestick charts
- Correlation heatmaps
- Moving average plots
- 30-day price forecasts

![AAPL Closing Price](https://github.com/user-attachments/assets/c62516a2-ccfa-4586-a140-dd2ed1b339a1)
![Average Daily return by Sector](https://github.com/user-attachments/assets/7ae3077f-1558-4237-aae0-54f6f8cc83fb)
![Stock Correlation matrix](https://github.com/user-attachments/assets/a1d22a9f-4870-4585-9425-02de034015c0)
![AAPL Price with moving averages](https://github.com/user-attachments/assets/72d5ddb0-dda9-419e-8109-58717f14dbe1)
![AAPL Price Forecast](https://github.com/user-attachments/assets/c3a23271-c9e5-47cd-87d1-05c7572da065)










