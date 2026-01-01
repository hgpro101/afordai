"""
Aford.ai - Today's Working Prototype
"""
import streamlit as st
from financial_calculator import *
from conversation_engine import *
from insights_generator import *

# Page configuration
st.set_page_config(
    page_title="Aford.ai - Your Gentle Financial Guide",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for gentle look
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: 500;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .big-font {
        font-size: 24px !important;
        font-weight: 300;
        color: #2E8B57;
    }
    .insight-box {
        background-color: #e8f5e9;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

# Header
st.title("🌱 Aford.ai")
st.markdown('<p class="big-font">Growing your financial confidence, gently.</p>', unsafe_allow_html=True)

st.markdown("---")

# Main flow based on step
if st.session_state.step == 0:
    # Welcome screen
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Welcome! I'm your gentle financial guide. 💬
        
        **I'm here to help you understand what you can afford, without pressure.**
        
        Today, let's explore **housing affordability** together.
        
        How it works:
        1. **You choose** how much to share (anonymous → casual → detailed)
        2. **I'll ask** gentle questions about your situation
        3. **You'll get** instant insights and "aha moments"
        4. **No accounts needed** - your privacy comes first
        
        Ready to begin?
        """)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=400", 
                caption="Your financial journey starts with curiosity")
    
    if st.button("🌟 Start Exploring", use_container_width=True):
        st.session_state.step = 1
        st.rerun()

elif st.session_state.step == 1:
    # Step 1: Dream about housing
    st.subheader("Step 1: Let's dream about housing 🏠")
    
    dream_home, timeline = ask_housing_preferences()
    st.session_state.user_data['dream_home'] = dream_home
    st.session_state.user_data['timeline'] = timeline
    
    if st.button("Continue →", key="step1_continue"):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    # Step 2: Gentle income questions
    st.subheader("Step 2: Let's talk about income gently 💰")
    
    st.info("💭 **Remember:** You control how much you share. More detail = more precise insights.")
    
    income_level = ask_income_question()
    
    if income_level:
        st.session_state.user_data['income_level'] = income_level
        income = get_income_input(income_level)
        st.session_state.user_data['monthly_income'] = income
        
        # Show instant insight
        with st.expander("💡 Instant Insight", expanded=True):
            insight = generate_income_insight(income, income_level)
            st.markdown(f'<div class="insight-box">{insight}</div>', unsafe_allow_html=True)
        
        if st.button("Continue →", key="step2_continue"):
            st.session_state.step = 3
            st.rerun()

elif st.session_state.step == 3:
    # Step 3: Current situation
    st.subheader("Step 3: Your current housing situation 📍")
    
    current_info = ask_current_situation()
    st.session_state.user_data['current_housing'] = current_info
    
    # Calculate affordability
    income = st.session_state.user_data.get('monthly_income', 5000)
    affordable_rent = calculate_max_affordable_rent(income)
    st.session_state.user_data['affordable_rent'] = affordable_rent
    
    # Show housing insight
    with st.expander("🏠 Housing Affordability Check", expanded=True):
        insight = generate_housing_insight(affordable_rent, current_info['amount'])
        st.markdown(f'<div class="insight-box">{insight}</div>', unsafe_allow_html=True)
        
        # Educational snippet
        st.markdown(generate_educational_snippet("28_36_rule"))
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("← Go Back", use_container_width=True):
            st.session_state.step = 2
            st.rerun()
    
    with col2:
        if st.button("See My Full Analysis →", use_container_width=True):
            st.session_state.step = 4
            st.rerun()

elif st.session_state.step == 4:
    # Step 4: Full analysis
    st.subheader("🎯 Your Personal Housing Analysis")
    
    # Get user data
    income = st.session_state.user_data.get('monthly_income', 5000)
    affordable_rent = st.session_state.user_data.get('affordable_rent', 1500)
    dream_home = st.session_state.user_data.get('dream_home', '')
    timeline = st.session_state.user_data.get('timeline', '')
    current_info = st.session_state.user_data.get('current_housing', {})
    
    # Create three columns for dashboard
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Monthly Income", f"${income:,.0f}")
        st.metric("Max Recommended Rent", f"${affordable_rent:,.0f}")
    
    with col2:
        st.metric("Housing Budget", "Healthy" if current_info.get('amount', 0) <= affordable_rent else "Review")
        st.metric("Timeline", timeline)
    
    with col3:
        st.metric("Data Comfort", st.session_state.user_data.get('income_level', 'casual').title())
        st.metric("Dream", dream_home.split(' ')[0])
    
    st.markdown("---")
    
    # Interactive calculator
    st.subheader("🔧 Try Different Scenarios")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        new_income = st.slider(
            "What if your income was:",
            min_value=1000,
            max_value=20000,
            value=int(income),
            step=500,
            format="$%d"
        )
        
        new_debts = st.slider(
            "And monthly debts were:",
            min_value=0,
            max_value=5000,
            value=0,
            step=100,
            format="$%d"
        )
    
    with col_right:
        new_affordable = calculate_max_affordable_rent(new_income, new_debts)
        
        st.markdown(f"""
        <div class="insight-box">
        <h4>💰 With these numbers:</h4>
        • Max affordable rent: <b>${new_affordable:,.0f}</b><br>
        • Should be ≤ <b>${int(new_income * 0.3):,.0f}</b> (30% rule)<br>
        • Leaves <b>${int(new_income - new_affordable - new_debts):,.0f}</b> for other expenses
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Next steps
    st.subheader("🚀 Your Personalized Next Steps")
    
    st.markdown(get_next_steps_recommendation(
        st.session_state.user_data.get('income_level', 'casual'),
        timeline
    ))
    
    # Educational snippets
    with st.expander("📚 Learn More", expanded=False):
        tab1, tab2, tab3 = st.tabs(["28/36 Rule", "Rent vs Buy", "First-Time Tips"])
        
        with tab1:
            st.markdown(generate_educational_snippet("28_36_rule"))
        
        with tab2:
            st.markdown(generate_educational_snippet("rent_vs_buy"))
        
        with tab3:
            st.markdown(generate_educational_snippet("downpayment"))
    
    st.markdown("---")
    
    # Restart or share
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Start New Conversation", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    with col2:
        if st.button("🏠 Explore Another Topic", use_container_width=True):
            st.session_state.step = 0
            st.rerun()
    
    with col3:
        st.info("👋 Session ends here. No data saved.")

# Sidebar with info
with st.sidebar:
    st.markdown("### 🌱 About Aford.ai")
    st.markdown("""
    **Today's Prototype Features:**
    • One complete conversation flow
    • Three privacy levels
    • Instant "aha moment" insights
    • Interactive calculators
    • Educational snippets
    
    **Coming Soon:**
    • More conversation topics
    • Goal tracking
    • Financial account integration
    • Mobile app
    
    *Built with care today. No data stored.*
    """)
    
    st.markdown("---")
    
    st.markdown("**Your Progress:**")
    if st.session_state.step == 0:
        st.progress(0)
    elif st.session_state.step == 1:
        st.progress(25)
    elif st.session_state.step == 2:
        st.progress(50)
    elif st.session_state.step == 3:
        st.progress(75)
    else:
        st.progress(100)
    
    st.markdown(f"**Step {st.session_state.step}/4**")