import pandas as pd
from analysis import monthly_expenses
from analysis import summary

def create_home_dict(home_price, monthly_rent, down_payment_percent, annual_interest_rate, loan_term, num_bathrooms, home_sqft):

    home_dict = {
        'Home Price' : home_price,
        'Monthly Rent' : monthly_rent,
        'Down Payment Percent' : down_payment_percent,
        'Annual Interest Rate' : annual_interest_rate,
        'Loan Term' : loan_term,
        'Number of Bathrooms' : num_bathrooms,
        'Home Square Footage' : home_sqft,
    }

    return home_dict




