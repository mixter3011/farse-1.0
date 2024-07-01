# The Data is from 2005 to 2024

import numpy as np
import pandas as pd

file_path = 'farse 1.0/Market Risk/Equity/data/NIFTY CORE HOUSING_Historical_PR_01011990to01072024.csv'
nifty_core_housing_data = pd.read_csv(file_path, parse_dates=['Date'])

nifty_core_housing_data.set_index('Date', inplace=True)

print(nifty_core_housing_data.head())

nifty_core_housing_data['Log Return'] = np.log(nifty_core_housing_data['Close'] / nifty_core_housing_data['Close'].shift(1))

nifty_core_housing_data.dropna(inplace=True)

confidence_level = 0.95

VaR = np.percentile(nifty_core_housing_data['Log Return'], (1 - confidence_level) * 100)
print(f"Value at Risk (VaR) at {confidence_level*100}% confidence level: {VaR}")
