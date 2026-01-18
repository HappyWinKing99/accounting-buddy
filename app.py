import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Accounting Buddy", page_icon="📊")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Ratio Calculator", "Flashcards"])

# --- PAGE 1: HOME ---
if page == "Home":
    st.title("📊 Accounting Study Buddy")
    st.write("Welcome to your personal accounting assistant.")
    st.info("Select a tool from the sidebar to get started.")
    
    st.subheader("Quick Reference")
    st.markdown("""
    * **Assets** = Liabilities + Equity
    * **Net Income** = Revenue - Expenses
    * **Breakeven** = Fixed Costs / (Price - Variable Costs)
    """)

# --- PAGE 2: RATIO CALCULATOR ---
elif page == "Ratio Calculator":
    st.title("🧮 Ratio Calculator")
    
    ratio_type = st.selectbox("Select a Ratio", ["Current Ratio", "Return on Equity (ROE)", "Profit Margin"])
    
    if ratio_type == "Current Ratio":
        st.write("Formula: **Current Assets / Current Liabilities**")
        assets = st.number_input("Current Assets ($)", min_value=0.0)
        liabilities = st.number_input("Current Liabilities ($)", min_value=0.0)
        
        if st.button("Calculate"):
            if liabilities > 0:
                result = assets / liabilities
                st.success(f"Current Ratio: {result:.2f}")
                if result > 1.5:
                    st.write("✅ Healthy Liquidity")
                else:
                    st.write("⚠️ Check Liquidity")
            else:
                st.error("Liabilities cannot be zero.")

    elif ratio_type == "Return on Equity (ROE)":
        st.write("Formula: **Net Income / Shareholder's Equity**")
        ni = st.number_input("Net Income ($)", value=0.0)
        equity = st.number_input("Shareholder's Equity ($)", min_value=0.0)
        
        if st.button("Calculate ROE"):
            if equity > 0:
                roe = (ni / equity) * 100
                st.success(f"ROE: {roe:.2f}%")
            else:
                st.error("Equity must be greater than 0.")

# --- PAGE 3: FLASHCARDS ---
elif page == "Flashcards":
    st.title("📝 Study Flashcards")
    
    # You can add more terms here easily!
    terms = {
        "Accrual Accounting": "Recording revenues/expenses when they are incurred, regardless of when cash is exchanged.",
        "Depreciation": "Allocating the cost of a tangible asset over its useful life.",
        "Amortization": "Spreading out the cost of an intangible asset (like a patent) over time."
    }
    
    term_choice = st.selectbox("Choose a term:", list(terms.keys()))
    
    if st.button("Show Definition"):
        st.info(terms[term_choice])
