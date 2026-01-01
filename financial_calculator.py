"""
Core financial formulas for affordability calculations
"""
def calculate_max_affordable_rent(monthly_income, monthly_debts=0):
    """
    Calculate maximum affordable rent using 28/36 rule
    """
    # Front-end ratio: housing costs ≤ 28% of gross monthly income
    front_end_max = monthly_income * 0.28
    
    # Back-end ratio: total debt ≤ 36% of gross monthly income
    total_debt_allowed = monthly_income * 0.36
    back_end_max = total_debt_allowed - monthly_debts
    
    # Return the more conservative limit
    return min(front_end_max, back_end_max)

def calculate_housing_budget(annual_income, downpayment=0, debt_payments=0, credit_score=700):
    """
    Calculate total affordable home price
    """
    monthly_income = annual_income / 12
    
    # Max monthly payment (PITI)
    max_monthly_payment = calculate_max_affordable_rent(monthly_income, debt_payments)
    
    # Estimate property taxes and insurance (simplified)
    estimated_taxes_insurance = max_monthly_payment * 0.25
    
    # Money available for mortgage payment
    mortgage_payment = max_monthly_payment - estimated_taxes_insurance
    
    # Interest rate based on credit score
    if credit_score >= 760:
        interest_rate = 0.065  # 6.5%
    elif credit_score >= 700:
        interest_rate = 0.07   # 7.0%
    elif credit_score >= 650:
        interest_rate = 0.075  # 7.5%
    else:
        interest_rate = 0.08   # 8.0%
    
    # Calculate loan amount (30-year fixed)
    monthly_rate = interest_rate / 12
    months = 30 * 12
    if monthly_rate > 0:
        loan_amount = mortgage_payment * ((1 - (1 + monthly_rate) ** -months) / monthly_rate)
    else:
        loan_amount = mortgage_payment * months
    
    # Total affordable price
    affordable_price = loan_amount + downpayment
    
    return {
        "affordable_price": round(affordable_price, 2),
        "max_monthly_payment": round(max_monthly_payment, 2),
        "loan_amount": round(loan_amount, 2),
        "interest_rate": interest_rate
    }

def calculate_rent_vs_buy(rent_amount, home_price, years_staying=5):
    """
    Simple rent vs buy comparison
    """
    # Simplified calculation
    annual_rent = rent_amount * 12
    annual_ownership_cost = home_price * 0.05  # 5% for mortgage, taxes, maintenance
    
    rent_total = annual_rent * years_staying
    buy_total = annual_ownership_cost * years_staying
    
    breakeven_years = 3  # Simplified
    
    return {
        "rent_total": rent_total,
        "buy_total": buy_total,
        "breakeven_years": breakeven_years,
        "recommendation": "Buy" if years_staying > breakeven_years else "Rent"
    }