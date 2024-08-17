import numpy as np
import pandas as pd
import re

class InterestRateVaRModel:
    def __init__(self, path, confidence_level=0.95):
        self.path = path
        self.confidence_level = confidence_level
        self.interest_rate_data = pd.read_csv(self.path)

    def clean_date(self, date_str):
        cleaned_data = re.search(r'\w+ \d{2}, \d{4}', date_str)
        return cleaned_data.group() if cleaned_data else date_str

    def preprocess_data(self):
        self.interest_rate_data['Release Date'] = self.interest_rate_data['Release Date'].apply(self.clean_date)
        self.interest_rate_data['Release Date'] = pd.to_datetime(self.interest_rate_data['Release Date'])

        self.interest_rate_data['Actual'] = self.interest_rate_data['Actual'].str.rstrip('%').astype(float)

        self.interest_rate_data = self.interest_rate_data.sort_values('Release Date')

        self.interest_rate_data['Interest Change (%)'] = self.interest_rate_data['Actual'].pct_change() * 100

        self.interest_rate_data = self.interest_rate_data.dropna(subset=['Interest Change (%)'])

    def calculate_var(self):
        VaR = np.percentile(self.interest_rate_data['Interest Change (%)'], (1 - self.confidence_level) * 100)
        return VaR

    def run(self):
        self.preprocess_data()
        VaR = self.calculate_var()
        return VaR

model = InterestRateVaRModel('farse 1.0/Market Risk/Interest/data/interest rate (2000 - 2024).csv')
var_result = model.run()
print(f'Value at Risk (VaR): {var_result}')
