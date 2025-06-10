# Stock Market Data Analysis

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/github/license/arc8de/stock_market_data_analysis)

## Overview

This project analyzes historical stock market data to identify trends, correlations, and predict future prices.  
It leverages Python, Pandas, Prophet, Matplotlib, and other libraries.  
Intended for students, analysts, and hobbyists interested in financial data science.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Changing the Analyzed Stocks](#changing-the-analyzed-stocks)
- [Features](#features)
- [Sample Outputs](#sample-outputs)
- [Data Source](#data-source)
- [Contributing](#contributing)
- [License](#license)

---

## Project Structure

```
📦 
├─ OUTPUT IMAGES
│  ├─ 2. AAPL CLOSING PRICE.png
│  ├─ 2. AAPL price with moving averages.png
│  ├─ 2. Average Daily Returns by Sector.png
│  ├─ 2. Stock Correlation matrix.png
│  └─ 3 .Final AAPL Price Forecast.png
├─ README.md
├─ notebooks
│  ├─ 1. Stock Data Cleaning.ipynb
│  ├─ 2. Exploratory Data Analysis.ipynb
│  ├─ 3. Predictive Modeling.ipynb
│  └─ data
│     ├─ sectors.csv
│     └─ stock_data.csv
├─ requirements.txt
└─ src
   ├─ data_processing.py
   └─ visualization.py
```

---

## Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/arc8de/stock_market_data_analysis.git
   cd stock_market_data_analysis
   ```

2. **Set up a virtual environment (recommended)**
   ```sh
   python3 -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```

3. **Install requirements**
   ```sh
   pip install -r requirements.txt
   ```
   or install the requiremnts onr at a time in your terminal in case of an error.

4. **Launch Jupyter Notebook**
   ```sh
   jupyter notebook
   ```
   Or use your preferred IDE.

---

## Usage

1. Run the notebooks in order:
   - `1. Stock Data Cleaning.ipynb` (Fetches live data from Yahoo Finance)
   - `2. Exploratory Data Analysis.ipynb`
   - `3. Predictive Modeling.ipynb`

2. By default, analysis is performed for a set of example tickers.  
   To analyze other stocks, see the section below.

**Note:** The sample output files use the default ticker symbol.  
You can update the ticker list in the notebooks to analyze different stocks.

---

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

**Tip:** You can find ticker symbols for companies on Yahoo Finance or Google Finance.

---

## Features

- Live data fetching from Yahoo Finance (using `yfinance`)
- Technical indicator calculation
- Interactive visualizations (Matplotlib)
- Price forecasting with Prophet
- Sector performance analysis

---

## Sample Outputs

- **Candlestick charts**  
  Visualize price movements and volatility for selected tickers.

- **Correlation heatmaps**  
  Show the relationships between stock returns, identifying clusters of highly correlated companies.

- **Moving average plots**  
  Trend analysis using short-term and long-term moving averages.

- **30-day price forecasts**  
  Time series forecasting using Prophet.

![AAPL Closing Price](https://github.com/user-attachments/assets/d0b52ac7-f863-4b74-a659-fc33c2baaa97)
*Apple's daily closing price.*

![Average Daily return by Sector](https://github.com/user-attachments/assets/68746489-d8ea-48fa-8928-771ac83ae7e5)
*Comparison of sector performance.*

![Stock Correlation matrix](https://github.com/user-attachments/assets/0f9c5fc6-3a93-4b52-9a41-04984085127a)
*Correlation between different stocks.*

![AAPL Price with moving averages](https://github.com/user-attachments/assets/eaa92fd1-5043-4f22-9c5f-bd73978c37c5)
*Moving averages crossover signals on AAPL.*

![AAPL Price Forecast](https://github.com/user-attachments/assets/011b73f5-c47e-46e0-b76d-066a8b93a7f0)
*30-day price forecast for AAPL (Apple) using Prophet.*

---

## Data Source

- **Stock data** is fetched live from [Yahoo Finance](https://finance.yahoo.com) via the `yfinance` Python library.
- No API keys or authentication required.
- Ticker symbols can be found on Yahoo Finance or Google Finance.

---

## Contributing

Contributions are welcome!
- Open an issue to discuss feature suggestions or bugs.
- Fork the repo and submit a pull request.
- Please follow PEP8 and best practices for Python data science projects.

---

## License

This project is licensed under the [MIT License](LICENSE).

---
