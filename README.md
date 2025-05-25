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
   - 1. Stock Data Cleaning.ipynb (Fetches live data)
   - 2. Exploratory Data Analysis.ipynb
   - 3. Predictive Modeling.ipynb

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

