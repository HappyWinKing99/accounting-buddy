import streamlit as st
import pandas as pd
import numpy as np

# --- 1. APP CONFIGURATION (Must be the first command) ---
st.set_page_config(page_title="Accounting Buddy", page_icon="📊")

# --- 2. SESSION STATE SETUP (The "Memory") ---
# This checks: "Has the user clicked continue yet?"
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def go_to_main():
    st.session_state.page = 'main'

# --- 3. WELCOME PAGE ---
if st.session_state.page == 'welcome':
    st.title("Welcome to your Accounting Study Buddy!")
    st.write("##### The ultimate tool for BYU Accounting Students")
    
    # Official BYU Marriott School Logo (pulled from Wikimedia Commons)
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/95/Logo_of_the_Marriott_School_of_Business.png", width=500)
    
    st.write("") # Spacer
    st.write("Click below to access your formulas, calculators, and study tools.")
    
    # The Button that changes the 'page' state to 'main'
    st.button("➡️ Continue to App", on_click=go_to_main)

# --- 4. MAIN APP (Hidden until "Continue" is clicked) ---
elif st.session_state.page == 'main':
    
    # --- SIDEBAR NAVIGATION ---
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Ratio Calculator", "Formula Cheatsheet", "Managerial Tools"])

    # --- PAGE 1: HOME ---
    if page == "Home":
        st.title("📊 Accounting Dashboard")
        st.info("Select a tool from the sidebar to get started.")
        st.write("### Quick Stats")
        col1, col2, col3 = st.columns(3)
        col1.metric("Formulas Loaded", "15")
        col2.metric("Days Until Finals", "45")
        col3.metric("Study Streak", "3 Days")

    # --- PAGE 2: RATIO CALCULATOR ---
    elif page == "Ratio Calculator":
        st.title("🧮 Ratio Calculator")
        ratio_type = st.selectbox("Select a Ratio", ["Current Ratio", "Return on Equity (ROE)"])
        
        if ratio_type == "Current Ratio":
            st.write("Formula: **Current Assets / Current Liabilities**")
            assets = st.number_input("Current Assets ($)", min_value=0.0)
            liabilities = st.number_input("Current Liabilities ($)", min_value=0.0)
            if st.button("Calculate"):
                if liabilities > 0:
                    st.success(f"Current Ratio: {assets/liabilities:.2f}")
                else:
                    st.error("Liabilities cannot be zero.")

        elif ratio_type == "Return on Equity (ROE)":
            st.write("Formula: **Net Income / Shareholder's Equity**")
            ni = st.number_input("Net Income ($)", value=0.0)
            equity = st.number_input("Shareholder's Equity ($)", min_value=0.0)
            if st.button("Calculate ROE"):
                if equity > 0:
                    st.success(f"ROE: {(ni/equity)*100:.2f}%")
                else:
                    st.error("Equity must be greater than 0.")

    # --- PAGE 3: FORMULA CHEATSHEET ---
    elif page == "Formula Cheatsheet":
        st.title("📚 Master Formula Database")
        
        # The Data
        data = {
            "Category": ["Financial", "Financial", "Managerial", "Managerial", "Tax", "Tax"],
            "Term": ["Current Ratio", "ROE", "Contribution Margin", "Break-Even Point", "Effective Tax Rate", "After-Tax Yield"],
            "Formula": ["Current Assets / Current Liabilities", "Net Income / Equity", "Sales - Variable Costs", "Fixed Costs / Unit CM", "Total Tax / Total Income", "Pre-Tax Yield * (1 - Tax Rate)"],
            "Description": ["Measures liquidity.", "Measures profitability.", "Profit available for fixed costs.", "Sales needed to cover costs.", "Avg rate of tax paid.", "Real return after taxes."]
        }
        df = pd.DataFrame(data)
        
        # Search Bar
        search_term = st.text_input("🔍 Search Formulas:")
        if search_term:
            filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        else:
            filtered_df = df
            
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    # --- PAGE 4: MANAGERIAL TOOLS ---
    elif page == "Managerial Tools":
        st.title("🏭 Break-Even Visualizer")
        
        price = st.number_input("Price per Unit ($)", value=50.0)
        vc = st.number_input("Variable Cost per Unit ($)", value=30.0)
        fc = st.number_input("Total Fixed Costs ($)", value=5000.0)
        
        if price > vc:
            bep_units = fc / (price - vc)
            st.metric("Break-Even Point", f"{bep_units:.0f} Units")
            
            # Graphing Logic
            units = np.linspace(0, bep_units * 2, 100)
            rev = units * price
            costs = fc + (units * vc)
            
            chart_data = pd.DataFrame({"Units": units, "Revenue": rev, "Costs": costs})
            st.line_chart(chart_data, x="Units", y=["Revenue", "Costs"], color=["#00FF00", "#FF0000"])
        else:
            st.error("Price must be > Variable Cost")
