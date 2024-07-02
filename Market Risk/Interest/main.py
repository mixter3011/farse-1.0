import numpy as np 
import pandas as pd
import re

path = 'farse 1.0/Market Risk/Interest/data/interest rate (2000 - 2024).csv'
interest_rate_data = pd.read_csv(path)

def clean (date_str):
    cleaned_data = re.search(r'\w+ \d{2}, \d{4}', date_str)
    return cleaned_data.group() if cleaned_data else date_str

interest_rate_data['Release Date'] = interest_rate_data['Release Date'].apply(clean)
interest_rate_data['Release Date'] = pd.to_datetime(interest_rate_data['Release Date'])
interest_rate_data['Actual'] = interest_rate_data['Actual'].str.rstrip('%').astype(float)
interest_rate_data = interest_rate_data.sort_values('Release Date')
interest_rate_data['Interest Change (%)'] = interest_rate_data['Actual'].pct_change() * 100
interest_rate_data = interest_rate_data.dropna(subset=['Interest Change (%)'])
interest_rate_data.head()

confidence_level = 0.95

VaR = np.percentile(interest_rate_data['Interest Change (%)'], (1 - confidence_level) * 100)
print(VaR)