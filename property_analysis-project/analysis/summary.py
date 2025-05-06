def get_monthly_cashflow(home_dict):

    home_dict['Cashflow'] = sum(home_dict.values())

    return home_dict

def cash_on_cash_return(home_dict, total_investment):

    CoCROI = (home_dict['Cashflow']*12)/total_investment

    return CoCROI



