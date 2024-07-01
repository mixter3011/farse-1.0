import pandas as pd
import numpy as np

files = [
    ('nifty_50_arbitrage_data', 'farse 1.0/Market Risk/Equity/data/NIFTY 50 ARBITRAGE_Historical_PR_01011990to01072024.csv'),
    ('nifty_50_futures_pr_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY 50 FUTURES PR_Historical_PR_01011990to01072024.csv'),
    ('nifty_50_futures_tr_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY 50 FUTURES TR_Historical_PR_01011990to01072024.csv'),
    ('nifty_50_historical_pr_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY 50_Historical_PR_01011990to01072024.csv'),
    ('nifty_100_historical_pr_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY 100_Historical_PR_01011990to01072024.csv'),
    ('nifty_200_historical_pr_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY 200_Historical_PR_01011990to01072024.csv'),
    ('nifty_500_historical_pr_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY 500_Historical_PR_01011990to01072024.csv'),
    ('nifty_alpha_50_historical_pr_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY ALPHA 50_Historical_PR_01011990to01072024.csv'),
    ('nifty_alpha_low_volatility_30_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY ALPHA LOW-VOLATILITY 30_Historical_PR_01011990to01072024.csv'),
    ('nifty_alpha_quality_low_volatile_30_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY ALPHA QUALITY LOW-VOLATILITY 30_Historical_PR_01011990to01072024.csv'),
    ('nifty_alpha_quality_value_low_volatile_30_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY ALPHA QUALITY VALUE LOW-VOLATILITY 30_Historical_PR_01011990to01072024.csv'),
    ('nifty_auto_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY AUTO_Historical_PR_01011990to01072024.csv'),
    ('nifty_bank_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY BANK_Historical_PR_01011990to01072024.csv'),
    ('nifty_commodities_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY COMMODITIES_Historical_PR_01011990to01072024.csv'),
    ('nifty_consumer_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY CONSUMER DURABLES_Historical_PR_01011990to01072024.csv'),
    ('nifty_core_housing_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY CORE HOUSING_Historical_PR_01011990to01072024.csv'),
    ('nifty_cpse_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY CPSE_Historical_PR_01011990to01072024.csv'),
    ('nifty_dividend_oppurtunity_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY DIVIDEND OPPORTUNITIES 50_Historical_PR_01011990to01072024.csv'),
    ('nifty_energy_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY ENERGY_Historical_PR_01011990to01072024.csv'),
    ('nifty_ev_new_age_automotive_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY EV & NEW AGE AUTOMOTIVE_Historical_PR_01011990to01072024.csv'),
    ('nifty_financial_services_25_50_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY FINANCIAL SERVICES 25_50_Historical_PR_01011990to01072024.csv'),
    ('nifty_financial_services_ex_bank_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY FINANCIAL SERVICES EX-BANK_Historical_PR_01011990to01072024.csv'),
    ('nifty_financial_services_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY FINANCIAL SERVICES_Historical_PR_01011990to01072024.csv'),
    ('nifty_fmcg_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY FMCG_Historical_PR_01011990to01072024.csv'),
    ('nifty_growth_sector_15_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY GROWTH SECTORS 15_Historical_PR_01011990to01072024.csv'),
    ('nifty_healthcare_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY HEALTHCARE_Historical_PR_01011990to01072024.csv'),
    ('nifty_high_beta_50_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY HIGH BETA 50_Historical_PR_01011990to01072024.csv'),
    ('nifty_housing_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY HOUSING_Historical_PR_01011990to01072024.csv'),
    ('nifty_india_consumption_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY INDIA CONSUMPTION_Historical_PR_01011990to01072024.csv'),
    ('nifty_aditya_birla_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY INDIA CORPORATE GROUP INDEX - ADITYA BIRLA GROUP_Historical_PR_01011990to01072024.csv'),
    ('nifty_mahindra_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY INDIA CORPORATE GROUP INDEX - MAHINDRA GROUP_Historical_PR_01011990to01072024.csv'),
    ('nifty_tata_group_25_percent_cap_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY INDIA CORPORATE GROUP INDEX - TATA GROUP 25% CAP_Historical_PR_01011990to01072024.csv'),
    ('nifty_tata_group_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY INDIA CORPORATE GROUP INDEX - TATA GROUP_Historical_PR_01011990to01072024.csv'),
    ('nifty_india_defence_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY INDIA DEFENCE_Historical_PR_01011990to01072024.csv'),
    ('nifty_india_digital_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY INDIA DIGITAL_Historical_PR_01011990to01072024.csv'),
    ('nifty_india_manufacturing_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY INDIA MANUFACTURING_Historical_PR_01011990to01072024.csv'),
    ('nifty_india_tourism_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY INDIA TOURISM_Historical_PR_01011990to01072024.csv'),
    ('nifty_infrastructure_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY INFRASTRUCTURE_Historical_PR_01011990to01072024.csv'),
    ('nifty_largemidcap_250_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY IT_Historical_PR_01011990to01072024.csv'),
    ('nifty_low_volatility_50_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY LARGEMIDCAP 250_Historical_PR_01011990to01072024.csv'),
    ('nifty_media_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY LOW VOLATILITY 50_Historical_PR_01011990to01072024.csv'),
    ('nifty_metal_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MEDIA_Historical_PR_01011990to01072024.csv'),
    ('nifty_microcap_250_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY METAL_Historical_PR_01011990to01072024.csv'),
    ('nifty_midcap_50_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MICROCAP 250_Historical_PR_01011990to01072024.csv'),
    ('nifty_midcap_100_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDCAP 50_Historical_PR_01011990to01072024.csv'),
    ('nifty_midcap_150_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDCAP 100_Historical_PR_01011990to01072024.csv'),
    ('nifty_midcap_liquid_15_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDCAP 150_Historical_PR_01011990to01072024.csv'),
    ('nifty_midcap_select_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDCAP LIQUID 15_Historical_PR_01011990to01072024.csv'),
    ('nifty_midcap_150_momentum_50_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDCAP SELECT_Historical_PR_01011990to01072024.csv'),
    ('nifty_midcap_150_quality_50_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDCAP150 MOMENTUM 50_Historical_PR_01011990to01072024.csv'),
    ('nifty_midsmall_financial_services_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDCAP150 QUALITY 50_Historical_PR_01011990to01072024.csv'),
    ('nifty_midsmall_healthcare_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDSMALL FINANCIAL SERVICES_Historical_PR_01011990to01072024.csv'),
    ('nifty_midsmall_india_consumption_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDSMALL HEALTHCARE_Historical_PR_01011990to01072024.csv'),
    ('nifty_midsmall_it_telecom_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDSMALL INDIA CONSUMPTION_Historical_PR_01011990to01072024.csv'),
    ('nifty_midsmallcap_400_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDSMALL IT & TELECOM_Historical_PR_01011990to01072024.csv'),
    ('nifty_midsmallcap_400_momentum_quality_100_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDSMALLCAP 400_Historical_PR_01011990to01072024.csv'),
    ('nifty_mnc_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MIDSMALLCAP400 MOMENTUM QUALITY 100_Historical_PR_01011990to01072024.csv'),
    ('nifty_mobility_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MNC_Historical_PR_01011990to01072024.csv'),
    ('nifty_next_50_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY MOBILITY_Historical_PR_01011990to01072024.csv'),
    ('nifty_non_cyclical_consumer_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY NEXT 50_Historical_PR_01011990to01072024.csv'),
    ('nifty_oil_gas_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY NON-CYCLICAL CONSUMER_Historical_PR_01011990to01072024.csv'),
    ('nifty_pharma_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY OIL & GAS_Historical_PR_01011990to01072024.csv'),
    ('nifty_private_bank_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY PHARMA_Historical_PR_01011990to01072024.csv'),
    ('nifty_pse_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY PRIVATE BANK_Historical_PR_01011990to01072024.csv'),
    ('nifty_psu_bank_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY PSE_Historical_PR_01011990to01072024.csv'),
    ('nifty_quality_low_volatile_30_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY PSU BANK_Historical_PR_01011990to01072024.csv'),
    ('nifty_realty_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY QUALITY LOW-VOLATILITY 30_Historical_PR_01011990to01072024.csv'),
    ('nifty_reits_invits_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY REALTY_Historical_PR_01011990to01072024.csv'),
    ('nifty_services_sector_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY REITS & INVITS_Historical_PR_01011990to01072024.csv'),
    ('nifty_shariah_25_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY SERVICES SECTOR_Historical_PR_01011990to01072024.csv'),
    ('nifty_smallcap_50_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY SHARIAH 25_Historical_PR_01011990to01072024.csv'),
    ('nifty_smallcap_100_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY SMALLCAP 50_Historical_PR_01011990to01072024.csv'),
    ('nifty_smallcap_250_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY SMALLCAP 100_Historical_PR_01011990to01072024.csv'),
    ('nifty_smallcap_250_momentum_quality_100_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY SMALLCAP 250_Historical_PR_01011990to01072024.csv'),
    ('nifty_smallcap_250_quality_50_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY SMALLCAP250 MOMENTUM QUALITY 100_Historical_PR_01011990to01072024.csv'),
    ('nifty_sme_emerge_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY SME EMERGE_Historical_PR_01011990to01072024.csv'),
    ('nifty_top_10_equal_weight_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY TOP 10 EQUAL WEIGHT_Historical_PR_01011990to01072024.csv'),
    ('nifty_total_market_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY TOTAL MARKET_Historical_PR_01011990to01072024.csv'),
    ('nifty_transportation_logistics_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY TRANSPORTATION & LOGISTICS_Historical_PR_01011990to01072024.csv'),
    ('nifty_dividend_points_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY50 DIVIDEND POINTS_Historical_PR_01011990to01072024.csv'),
    ('nifty_equal_weight_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY50 EQUAL WEIGHT_Historical_PR_01011990to01072024.csv'),
    ('nifty_pr_1x_inverse_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY50 PR 1X INVERSE_Historical_PR_01011990to01072024.csv'),
    ('nifty_pr_2x_levarage_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY50 PR 2X LEVERAGE_Historical_PR_01011990to01072024.csv'),
    ('nifty_shariah_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY50 SHARIAH_Historical_PR_01011990to01072024.csv'),
    ('nifty_50_tr_1x_inverse_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY50 TR 1X INVERSE_Historical_PR_01011990to01072024.csv'),
    ('nifty_50_tr_2x_leverage_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY50 TR 2X LEVERAGE_Historical_PR_01011990to01072024.csv'),
    ('nifty_50_usd_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY50 USD_Historical_PR_01011990to01072024.csv'),
    ('nifty_50_value_20_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY50 VALUE 20_Historical_PR_01011990to01072024.csv'),
    ('nifty_100_alpha_30_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY100 ALPHA 30_Historical_PR_01011990to01072024.csv'),
    ('nifty_100_enhanced_esg_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY100 ENHANCED ESG_Historical_PR_01011990to01072024.csv'),
    ('nifty_100_equal_weight_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY100 EQUAL WEIGHT_Historical_PR_01011990to01072024.csv'),
    ('nifty_100_esg_sector_leaders_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY100 ESG SECTOR LEADERS_Historical_PR_01011990to01072024.csv'),
    ('nifty_100_esg_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY100 ESG_Historical_PR_01011990to01072024.csv'),
    ('nifty_100_liquid_15_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY100 LIQUID 15_Historical_PR_01011990to01072024.csv'),
    ('nifty_100_low_volatility_30_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY100 LOW VOLATILITY 30_Historical_PR_01011990to01072024.csv'),
    ('nifty_100_quality_30_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY100 QUALITY 30_Historical_PR_01011990to01072024.csv'),
    ('nifty_200_alpha_30_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY200 ALPHA 30_Historical_PR_01011990to01072024.csv'),
    ('nifty_200_momentum_30_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY200 MOMENTUM 30_Historical_PR_01011990to01072024.csv'),
    ('nifty_200_quality_30_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY200 QUALITY 30_Historical_PR_01011990to01072024.csv'),
    ('nifty_200_value_30_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY200 VALUE 30_Historical_PR_01011990to01072024.csv'),
    ('nifty_500_equal_weight_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY500 EQUAL WEIGHT_Historical_PR_01011990to01072024.csv'),
    ('nifty_500_largemidsmall_equal_cap_weighted_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY500 LARGEMIDSMALL EQUAL-CAP WEIGHTED_Historical_PR_01011990to01072024.csv'),
    ('nifty_500_momentum_50_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY500 MOMENTUM 50_Historical_PR_01011990to01072024.csv'),
    ('nifty_500_multiap_50_25_25_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY500 MULTICAP 50_25_25_Historical_PR_01011990to01072024.csv'),
    ('nifty_500_multicap_india_manufacturing_50_30_20_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY500 MULTICAP INDIA MANUFACTURING 50_30_20_Historical_PR_01011990to01072024.csv'),
    ('nifty_500_multicap_infrastructure_50_30_20_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY500 MULTICAP INFRASTRUCTURE 50_30_20_Historical_PR_01011990to01072024.csv'),
    ('nifty_500_shariah_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY500 SHARIAH_Historical_PR_01011990to01072024.csv'),
    ('nifty_500_value_50_data' , 'farse 1.0/Market Risk/Equity/data/NIFTY500 VALUE 50_Historical_PR_01011990to01072024.csv')

]

dataframes = {}

for name, path in files:
    dataframes[name] = pd.read_csv(path)

def calculate_var(df, confidence_level=0.95):
    # Assume the last column is the price
    returns = df.iloc[:, -1].pct_change().dropna()
    var = np.percentile(returns, (1 - confidence_level) * 100)
    return var

var_results = {}

for name, df in dataframes.items():
    var_results[name] = calculate_var(df)

for name, var in var_results.items():
    print(f"{name}: VaR = {var}")


