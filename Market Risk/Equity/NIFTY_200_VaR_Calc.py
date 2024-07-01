import numpy as np
import pandas as pd

file_path = 'farse 1.0/Market Risk/Equity/data/NIFTY 200_Historical_PR_03102011to01072024.csv'
nifty_200_data = pd.read_csv(file_path, parse_dates=['Date'])

nifty_200_data.set_index('Date', inplace=True)

print(nifty_200_data.head())

nifty_200_data['Log Return'] = np.log(nifty_200_data['Close'] / nifty_200_data['Close'].shift(1))

nifty_200_data.dropna(inplace=True)

confidence_level = 0.95

VaR = np.percentile(nifty_200_data['Log Return'], (1 - confidence_level) * 100)
print(f"Value at Risk (VaR) at {confidence_level*100}% confidence level: {VaR}")

