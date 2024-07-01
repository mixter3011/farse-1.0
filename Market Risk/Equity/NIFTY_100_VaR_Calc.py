# The Data is from 2003 to 2024

import numpy as np
import pandas as pd

file_path = 'farse 1.0/Market Risk/Equity/data/NIFTY 100_Historical_PR_01011990to01072024.csv'
nifty_100_data = pd.read_csv(file_path, parse_dates=['Date'])

nifty_100_data.set_index('Date', inplace=True)

print(nifty_100_data.head())

nifty_100_data['Log Return'] = np.log(nifty_100_data['Close'] / nifty_100_data['Close'].shift(1))

nifty_100_data.dropna(inplace=True)

confidence_level = 0.95

VaR = np.percentile(nifty_100_data['Log Return'], (1 - confidence_level) * 100)
print(f"Value at Risk (VaR) at {confidence_level*100}% confidence level: {VaR}")

