import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class RiskAnalysisModel:
    def __init__(self, file_path, confidence_level=0.95):
        self.file_path = file_path
        self.confidence_level = confidence_level
        self.exchange_rate_data = None
        self.currency_columns = {
            'US Dollar': 'USD',
            'Pound Sterling': 'GBP',
            'Euro': 'Euro',
            'Japanese Yen': 'Yen'
        }
        self.vars = {}

    def load_data(self):
        """Load the exchange rate data from the CSV file."""
        self.exchange_rate_data = pd.read_csv(self.file_path, parse_dates=['Date'])
        self.exchange_rate_data.set_index('Date', inplace=True)

    def calculate_log_returns(self):
        """Calculate log returns for each currency."""
        for column_name, currency in self.currency_columns.items():
            log_return_column = f'Log Return {currency}'
            self.exchange_rate_data[log_return_column] = np.log(
                self.exchange_rate_data[column_name] / self.exchange_rate_data[column_name].shift(1)
            )
        self.exchange_rate_data.dropna(inplace=True)

    def plot_log_returns(self):
        """Plot the log returns for each currency."""
        plt.figure(figsize=(14, 10))
        for i, currency in enumerate(self.currency_columns.values(), 1):
            plt.subplot(2, 2, i)
            log_return_column = f'Log Return {currency}'
            self.exchange_rate_data[log_return_column].plot(title=f'Log Returns of {currency} to INR')
            plt.xlabel('Date')
            plt.ylabel('Log Return')
        plt.tight_layout()
        plt.show()

    def calculate_var(self):
        """Calculate the Value at Risk (VaR) for each currency."""
        for currency in self.currency_columns.values():
            log_return_column = f'Log Return {currency}'
            var = np.percentile(self.exchange_rate_data[log_return_column], (1 - self.confidence_level) * 100)
            self.vars[currency] = var

    def summarize_statistics(self):
        """Generate summary statistics for the dataset."""
        return self.exchange_rate_data.describe()

    def run_analysis(self):
        """Run the full analysis process."""
        self.load_data()
        self.calculate_log_returns()
        self.plot_log_returns()
        self.calculate_var()
        summary_stats = self.summarize_statistics()
        return summary_stats, self.vars


file_path = 'farse 1.0/Market Risk/Currency/data/exchange_rate_data.csv'
model = RiskAnalysisModel(file_path)
summary_stats, vars = model.run_analysis()

print("Summary Statistics:")
print(summary_stats)
print("\nValue at Risk (VaR):")
print(vars)
