def summarize_investment(home_dict, monthly_expenses_dict, total_project_cost_dict):

    cashflow = home_dict['Monthly Rent'] - sum(monthly_expenses_dict.values())
    total_cash_needed = sum(total_project_cost_dict.values()) - home_dict['Loan Amount']

    summary_dict = {
        'Cashflow' : cashflow,
        'Total Cash Needed' : total_cash_needed,
        'Cash on Cash Return on Investment' : (cashflow*12)/total_cash_needed

    }

    return summary_dict











def create_estimated_repairs_cost_dict(home_dict):

    estimated_repairs_dict = {
        'Kitchen Remodel' : calculate_kitchen_remodel_expense(home_sqft=home_dict['Home Square Footage']),
        'Bathroom Remodel' : calculate_bathroom_remodel_expense(num_bathrooms=home_dict['Number of Bathrooms'])
    }
    
    return estimated_repairs_dict



def get_total_project_cost_dict(home_dict, monthly_expenses_dict, estimated_repairs_dict):

    total_project_cost_dict = {
        'Home Price' : home_dict['Home Price'],
        'Purchase Closing' : calculate_purchase_closing_costs(home_dict=home_dict),
        'Pre Rent Holding' : calculate_pre_rent_holding_costs(monthly_expenses_dict=monthly_expenses_dict),
        'Estimated Repairs' : calculate_estimated_repairs(estimated_repairs_dict=estimated_repairs_dict)

    }

    return total_project_cost_dict


def calculate_estimated_repairs(estimated_repairs_dict):


    estimated_repairs = sum(estimated_repairs_dict.values())

    return estimated_repairs



def calculate_total_cash_needed(total_project_cost, loan_amount):
    
    total_cash_needed = total_project_cost-loan_amount

    return total_cash_needed

def calculate_purchase_closing_costs(home_dict):

    closing_costs = 0.03 * home_dict['Loan Amount']

    return closing_costs

def calculate_kitchen_remodel_expense(home_sqft):

    # According to fabuwood Kitchens generally take up to 10-15% of home sqft
    kitchen_sqft = home_sqft*0.10

    # According to homeguide kitchen remodels generally take about $150-$250 per sqft
    kitchen_remodel_expense = kitchen_sqft * 200

    return kitchen_remodel_expense

def calculate_bathroom_remodel_expense(num_bathrooms):

    # Withorpe Design and Rebuild says average full bathroom is 60 sqft
    bathroom_sqft = num_bathrooms*60

    bathroom_remodel_expense = bathroom_sqft*200

    return bathroom_remodel_expense

def calculate_pre_rent_holding_costs(monthly_expenses_dict):

    one_month_holding_cost = sum(monthly_expenses_dict.values())

    pre_rent_holding_costs = -(one_month_holding_cost * 3)

    return pre_rent_holding_costs