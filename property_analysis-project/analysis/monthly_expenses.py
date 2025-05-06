def create_expense_dict(home_dict):

    monthly_expenses_dict = {
        'Mortgage': get_mortgage_expense(home_price=home_dict['Home Price'], down_payment_percent=home_dict['Down Payment Percent'], annual_interest_rate=home_dict['Annual Interest Rate'], loan_term=home_dict['Loan Term']),
        'Taxes': get_tax_expense(home_price=home_dict['Home Price']), 
        'Insurance': get_insurance_expense(), 
        'Flood Insurance': 0, 
        'Vacancy': calculate_vacancy_expense(monthly_rent=home_dict['Monthly Rent']), 
        'Repairs': get_repairs_cost(monthly_rent=home_dict['Monthly Rent']), 
        'Capital Expenditures': get_capex_expense(monthly_rent=home_dict['Monthly Rent']), 
        'Water': 0, 
        'Sewer': 0, 
        'Gargabe': 0, 
        'Gas': 0, 
        'Electricity': 0, 
        'HOA fees': 0, 
        'Snow removal': 0, 
        'Lawn care': 0, 
        'Property management': get_property_management_expense(monthly_rent=home_dict['Monthly Rent'])
    }

    return monthly_expenses_dict

def get_tax_expense(home_price):

    propert_tax_rate = 0.0205

    annual_tax_expense = home_price * propert_tax_rate

    monthly_tax_expense = -(annual_tax_expense / 12)

    return monthly_tax_expense

def calculate_vacancy_expense(monthly_rent):

    monthly_vacancy_expense = -(monthly_rent * 0.05)

    return monthly_vacancy_expense 

def get_insurance_expense():

    monthly_insurance_expense = -250

    return monthly_insurance_expense

def get_repairs_cost(monthly_rent):

    monthly_repairs = -(monthly_rent * 0.05)

    return monthly_repairs

def get_capex_expense(monthly_rent):

    monthly_capex = -(0.10 * monthly_rent)

    return monthly_capex
    
def get_property_management_expense(monthly_rent):

    monthly_property_management_expense = -(monthly_rent * 0.11)

    return monthly_property_management_expense

def get_mortgage_expense(home_price, down_payment_percent, annual_interest_rate, loan_term):

    principal_loan_amount = home_price*(1-down_payment_percent)

    monthly_interest_rate = annual_interest_rate/12

    number_of_loan_payments = loan_term*12

    monthly_payment = -(monthly_interest_rate * principal_loan_amount * ((1+monthly_interest_rate)**number_of_loan_payments) ) / (((1+monthly_interest_rate)**number_of_loan_payments) - 1)

    return monthly_payment

