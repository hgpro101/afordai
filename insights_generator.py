"""
Generate educational insights and "aha moments"
"""
def generate_income_insight(income, level):
    """
    Provide instant insight about income
    """
    insights = {
        "anonymous": [
            f"💡 In that range, housing should typically be under ${int(income * 0.3):,} monthly",
            f"🎯 People in this range often save 10-20% for major goals",
            f"📊 This puts you in a comfortable position for most cities!"
        ],
        "casual": [
            f"📈 With ${income:,.0f} monthly, you have good flexibility",
            f"💭 Did you know? At this income, financial experts recommend keeping housing under ${int(income * 0.3):,}",
            f"🎯 This income level allows for solid savings while enjoying life"
        ],
        "detailed": [
            f"🎯 Excellent clarity! ${income:,.0f} monthly gives you precise planning power",
            f"📊 At this exact income, aim for housing costs under ${int(income * 0.3):,} monthly",
            f"💡 Pro tip: Try saving ${int(income * 0.2):,} monthly for maximum financial growth"
        ]
    }
    
    import random
    return random.choice(insights[level])

def generate_housing_insight(affordable_rent, current_rent):
    """
    Insight about housing affordability
    """
    if current_rent == 0:
        return "🏠 Based on your income, your ideal rent should be under ${:,.0f} monthly".format(affordable_rent)
    
    ratio = (current_rent / affordable_rent) * 100
    
    if ratio > 120:
        return f"⚠️ Your current rent (${current_rent:,.0f}) is {ratio:.0f}% of your recommended max. This might be stretching your budget."
    elif ratio > 100:
        return f"📊 Your current rent (${current_rent:,.0f}) is at the upper limit of affordability. Consider if this aligns with your priorities."
    elif ratio > 80:
        return f"✅ Your current rent (${current_rent:,.0f}) is comfortably within your means at {ratio:.0f}% of your max."
    else:
        return f"🎉 Excellent! Your current rent (${current_rent:,.0f}) leaves room in your budget for other goals."

def generate_educational_snippet(topic):
    """
    Quick educational facts
    """
    snippets = {
        "28_36_rule": """
        **The 28/36 Rule:**
        • Housing costs ≤ 28% of your gross monthly income
        • Total debt payments ≤ 36% of your gross monthly income
        
        This rule helps ensure you don't become "house poor"!
        """,
        
        "rent_vs_buy": """
        **Rent vs Buy Rule of Thumb:**
        • **Rent** if you plan to move within 3-5 years
        • **Buy** if you'll stay longer (builds equity!)
        • Always factor in maintenance (1% of home value/year)
        """,
        
        "emergency_fund": """
        **Emergency Fund First:**
        Before major purchases, save 3-6 months of expenses.
        This protects you from unexpected job loss or emergencies.
        """,
        
        "downpayment": """
        **The 20% Down Payment Myth:**
        • Ideal but not always necessary
        • Many programs accept 3-10% down
        • Less down payment = higher monthly payments + PMI insurance
        """
    }
    
    return snippets.get(topic, "💡 Learning about finances empowers better decisions!")

def get_next_steps_recommendation(income_level, timeline):
    """
    Suggest next steps based on user's situation
    """
    if timeline in ["<1 year", "1-3 years"]:
        return """
        **🚀 Your Action Plan:**
        1. **This month:** Check your credit score (free at AnnualCreditReport.com)
        2. **Next 3 months:** Save for closing costs (2-5% of home price)
        3. **Next 6 months:** Get pre-approved by a lender
        4. **Ongoing:** Track your spending to maximize savings
        """
    elif timeline in ["3-5 years", "5+ years"]:
        return """
        **🌱 Your Growth Plan:**
        1. **This month:** Open a high-yield savings account for your down payment
        2. **This year:** Increase your income through skills/certifications
        3. **Next 2 years:** Pay down high-interest debt
        4. **Long-term:** Invest in retirement accounts for compound growth
        """
    else:  # Just dreaming
        return """
        **✨ Your Exploration Plan:**
        1. **This week:** Explore different neighborhoods online
        2. **This month:** Talk to friends about their home-buying experiences
        3. **Next 3 months:** Learn about different mortgage types
        4. **When ready:** Come back for personalized calculations!
        """