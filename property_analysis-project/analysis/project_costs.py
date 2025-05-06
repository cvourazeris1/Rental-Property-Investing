def create_estimated_repairs_cost_dict(home_dict):

    estimated_repairs_dict = {
        'Kitchen Remodel' : calculate_kitchen_remodel_expense(home_sqft=home_dict['Home Square Footage']),
        'Bathroom Remodel' : calculate_bathroom_remodel_expense(num_bathrooms=home_dict['Number of Bathrooms'])
    }
    
    return estimated_repairs_dict



def get_total_project_cost(purchase_price, purchase_closing_costs, pre_rent_holding_cost, estimated_repairs):

    total_project_cost = purchase_price + purchase_closing_costs + pre_rent_holding_cost + estimated_repairs

    return total_project_cost

def calculate_total_cash_needed(total_project_cost, loan_amount):
    
    total_cash_needed = total_project_cost-loan_amount

    return total_cash_needed

def calculate_purchase_closing_costs(loan_amount):

    closing_costs = 0.03 * loan_amount

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