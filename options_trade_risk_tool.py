import pandas as pd
import numpy as np

def calculate_portfolio_value(option_prices, option_quantities, commodity_price):
    option_values = option_prices * option_quantities
    total_value = option_values.sum() + commodity_price
    return total_value

def calculate_portfolio_risk(option_prices, option_quantities, commodity_price):
    option_values = option_prices * option_quantities
    option_variances = np.var(option_values)
    commodity_variance = np.var(commodity_price)
    portfolio_risk = np.sqrt(option_variances + commodity_variance)
    return portfolio_risk

option_prices = pd.Series([2.5, 3.2, 1.8])  
option_quantities = pd.Series([10, -5, 7]) 
commodity_price = 100.0 

portfolio_value = calculate_portfolio_value(option_prices, option_quantities, commodity_price)
portfolio_risk = calculate_portfolio_risk(option_prices, option_quantities, commodity_price)

print("Portfolio Value: $", portfolio_value)
print("Portfolio Risk: $", portfolio_risk)
