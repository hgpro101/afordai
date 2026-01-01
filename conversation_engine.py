"""
Gentle, progressive question asking
"""
import streamlit as st

def ask_income_question():
    """
    Ask about income in a gentle, non-threatening way
    """
    st.subheader("💰 Let's talk about income gently")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Anonymous**")
        st.markdown("Just curious ranges")
        if st.button("Broad Strokes", key="income_anonymous"):
            st.session_state['income_level'] = 'anonymous'
            return 'anonymous'
    
    with col2:
        st.markdown("**Casual**")
        st.markdown("Approximate numbers")
        if st.button("Ballpark Figures", key="income_casual"):
            st.session_state['income_level'] = 'casual'
            return 'casual'
    
    with col3:
        st.markdown("**Detailed**")
        st.markdown("Exact numbers")
        if st.button("Specific Details", key="income_detailed"):
            st.session_state['income_level'] = 'detailed'
            return 'detailed'
    
    return None

def get_income_input(level):
    """
    Get income based on chosen comfort level
    """
    if level == 'anonymous':
        st.info("💭 No exact numbers needed!")
        income_range = st.select_slider(
            "Which range feels closest to your monthly take-home?",
            options=["Under $2,000", "$2,000-$4,000", "$4,000-$6,000", 
                    "$6,000-$8,000", "Over $8,000"],
            value="$4,000-$6,000"
        )
        
        # Convert range to approximate midpoint for calculations
        range_map = {
            "Under $2,000": 1500,
            "$2,000-$4,000": 3000,
            "$4,000-$6,000": 5000,
            "$6,000-$8,000": 7000,
            "Over $8,000": 9000
        }
        return range_map[income_range]
    
    elif level == 'casual':
        st.info("🎯 Approximate is perfect!")
        income_approx = st.slider(
            "About what's your monthly take-home pay?",
            min_value=1000,
            max_value=20000,
            value=5000,
            step=500,
            format="$%d"
        )
        return income_approx
    
    else:  # detailed
        st.success("📊 Exact numbers help precise planning!")
        income_exact = st.number_input(
            "What's your exact monthly take-home?",
            min_value=0,
            max_value=50000,
            value=5000,
            step=100,
            format="$%d"
        )
        return income_exact

def ask_housing_preferences():
    """
    Gentle questions about housing preferences
    """
    st.subheader("🏠 Dream a little...")
    
    dream_home = st.radio(
        "Imagine your ideal home in 3 years:",
        ["Renting an apartment in the city 🏙️",
         "Owning a cozy starter home 🏡", 
         "Living mortgage-free in a paid-off home 🎉",
         "Something unique to me! ✨"]
    )
    
    timeline = st.select_slider(
        "When might you consider moving?",
        options=["Just dreaming", "5+ years", "3-5 years", "1-3 years", "<1 year"],
        value="Just dreaming"
    )
    
    return dream_home, timeline

def ask_current_situation():
    """
    Questions about current housing
    """
    st.subheader("📍 Your current situation")
    
    current_type = st.radio(
        "You currently:",
        ["Rent", "Own", "Live with family", "Other"]
    )
    
    if current_type == "Rent":
        rent_amount = st.slider(
            "Monthly rent (if comfortable sharing):",
            min_value=0,
            max_value=10000,
            value=1500,
            step=100,
            format="$%d"
        )
        return {"type": "rent", "amount": rent_amount}
    
    elif current_type == "Own":
        mortgage = st.slider(
            "Monthly mortgage payment:",
            min_value=0,
            max_value=10000,
            value=2000,
            step=100,
            format="$%d"
        )
        return {"type": "own", "amount": mortgage}
    
    return {"type": current_type, "amount": 0}