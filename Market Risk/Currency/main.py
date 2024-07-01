import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'farse 1.0/Market Risk/Currency/data/exchange_rate_data.csv'
exchange_rate_data = pd.read_csv(file_path, parse_dates=['Date'])

exchange_rate_data.set_index('Date', inplace=True)

currency_columns = {
    'US Dollar': 'USD',
    'Pound Sterling': 'GBP',
    'Euro': 'Euro',
    'Japanese Yen': 'Yen'
}

for column_name, currency in currency_columns.items():
    log_return_column = f'Log Return {currency}'
    exchange_rate_data[log_return_column] = np.log(exchange_rate_data[column_name] / exchange_rate_data[column_name].shift(1))

exchange_rate_data.dropna(inplace=True)

summary_stats = exchange_rate_data.describe()

plt.figure(figsize=(14, 10))
for i, currency in enumerate(currency_columns.values(), 1):
    plt.subplot(2, 2, i)
    log_return_column = f'Log Return {currency}'
    exchange_rate_data[log_return_column].plot(title=f'Log Returns of {currency} to INR')
    plt.xlabel('Date')
    plt.ylabel('Log Return')

plt.tight_layout()
plt.show()

confidence_level = 0.95 # this is technically the alpha value
vars = {}
for currency in currency_columns.values():
    log_return_column = f'Log Return {currency}'
    var = np.percentile(exchange_rate_data[log_return_column], (1 - confidence_level) * 100)
    vars[currency] = var

print(summary_stats, vars)
