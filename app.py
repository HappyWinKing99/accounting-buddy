import streamlit as st
import pandas as pd
import numpy as np

# --- 1. APP CONFIGURATION (Must be the first command) ---
# This sets the browser tab title, icon, AND forces dark mode
st.set_page_config(
    page_title="Accounting Buddy", 
    page_icon="📊",
    initial_sidebar_state="collapsed",  # Hides sidebar on welcome page
    layout="centered"
)

# Force dark mode with custom theme
st.markdown("""
    <style>
    /* Force dark background everywhere */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    
    /* Make top header bar black */
    header[data-testid="stHeader"] {
        background-color: #0E1117 !important;
    }
    
    /* Change all text to white for contrast */
    .stApp, .stMarkdown, p, span, div, label {
        color: #FFFFFF !important;
    }
    
    /* Professional font throughout app */
    .stApp {
        font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    }
    
    /* Sidebar styling - match dark theme */
    section[data-testid="stSidebar"] {
        background-color: #0E1117 !important;
    }
    
    section[data-testid="stSidebar"] > div {
        background-color: #0E1117 !important;
    }
    
    /* Sidebar text white */
    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    
    /* Sidebar radio buttons */
    section[data-testid="stSidebar"] .row-widget.stRadio > div {
        background-color: #1E1E1E !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }
    
    /* Sidebar title */
    section[data-testid="stSidebar"] h1 {
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. SESSION STATE SETUP (The "Memory") ---
# Session state is like the app's memory - it remembers things even when the page updates
# This checks: "Has the user clicked continue yet?"
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'  # Start on welcome page

# Track which class is selected from home page
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = None

# This function changes the page to 'main' when button is clicked
def go_to_main():
    st.session_state.page = 'main'

# --- 3. WELCOME PAGE ---
if st.session_state.page == 'welcome':
    # Add spacing from top
    st.write("")
    st.write("")
    st.write("")
    
    # Center everything using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # BYU Accounting Logo - Square with rounded corners
        st.markdown("""
            <div style='text-align: center;'>
                <svg width="220" height="220" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                    <rect x="5" y="5" width="90" height="90" rx="8" ry="8" fill="#002E5D"/>
                    <text x="50" y="42" font-size="22" fill="white" text-anchor="middle" font-weight="bold" font-family="Segoe UI, Helvetica, Arial, sans-serif">BYU</text>
                    <text x="50" y="65" font-size="10" fill="white" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" letter-spacing="1">ACCOUNTING</text>
                </svg>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        
        # Centered welcome message
        st.markdown("<h1 style='text-align: center;'>Welcome to your Accounting Study Buddy!</h1>", unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        st.write("")
        
        # Custom styled button using HTML/CSS for royal blue square
        button_clicked = st.button("GO", on_click=go_to_main, use_container_width=True)
        
    # Custom CSS to style the button
    st.markdown("""
        <style>
        /* Make button royal blue and square-ish */
        .stButton > button {
            background-color: #002E5D !important;
            color: white !important;
            font-size: 24px !important;
            font-weight: bold !important;
            padding: 20px 60px !important;
            border-radius: 8px !important;
            border: none !important;
        }
        .stButton > button:hover {
            background-color: #003D7A !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 4. MAIN APP (Hidden until "Continue" is clicked) ---
elif st.session_state.page == 'main':
    
    # --- SIDEBAR NAVIGATION ---
    st.sidebar.title("📚 Navigation")
    
    # If user clicked a course box from home, switch to that page
    if st.session_state.selected_page:
        page = st.session_state.selected_page
        st.session_state.selected_page = None  # Reset after using
    else:
        # Radio buttons create a selection menu - only one can be selected at a time
        page = st.sidebar.radio(
            "Select Your Class:", 
            ["🏠 Home", "ACC 200 - Intro", "ACC 310 - Intermediate I", "ACC 401 - Intermediate II", "ACC 402 - Cost Accounting", "🧮 Calculators"]
        )

    # --- PAGE 1: HOME ---
    if page == "🏠 Home":
        # Centered title in blue square box
        st.markdown("""
            <div style='text-align: center; margin-bottom: 40px;'>
                <div style='background-color: #002E5D; padding: 25px; border-radius: 12px; display: inline-block;'>
                    <h1 style='color: white; margin: 0; font-family: Segoe UI, Helvetica, Arial, sans-serif;'>BYU ACCOUNTING DASHBOARD</h1>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.info("👇 Select a class below to view formulas and concepts!")
        
        st.write("")
        st.write("### 📖 Select Your Class")
        st.write("")
        
        # Create clickable course boxes
        col1, col2 = st.columns(2)
        
        with col1:
            # ACC 200 Box
            st.markdown("""
                <div style='background-color: #002E5D; padding: 25px; border-radius: 12px; margin-bottom: 20px; cursor: pointer;'>
                    <h3 style='color: white; margin: 0;'>📘 ACC 200</h3>
                    <p style='color: white; margin: 10px 0 0 0;'><strong>Introduction to Accounting</strong></p>
                    <p style='color: #B0B0B0; margin: 5px 0 0 0; font-size: 14px;'>Basic principles, financial statements, journal entries</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Go to ACC 200", key="btn_acc200", use_container_width=True):
                st.session_state.selected_page = "ACC 200 - Intro"
                st.rerun()
            
            st.write("")
            
            # ACC 401 Box
            st.markdown("""
                <div style='background-color: #002E5D; padding: 25px; border-radius: 12px; margin-bottom: 20px;'>
                    <h3 style='color: white; margin: 0;'>📙 ACC 401</h3>
                    <p style='color: white; margin: 10px 0 0 0;'><strong>Intermediate Accounting II</strong></p>
                    <p style='color: #B0B0B0; margin: 5px 0 0 0; font-size: 14px;'>Long-term assets, liabilities, bonds, leases</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Go to ACC 401", key="btn_acc401", use_container_width=True):
                st.session_state.selected_page = "ACC 401 - Intermediate II"
                st.rerun()
        
        with col2:
            # ACC 310 Box
            st.markdown("""
                <div style='background-color: #002E5D; padding: 25px; border-radius: 12px; margin-bottom: 20px;'>
                    <h3 style='color: white; margin: 0;'>📗 ACC 310</h3>
                    <p style='color: white; margin: 10px 0 0 0;'><strong>Intermediate Accounting I</strong></p>
                    <p style='color: #B0B0B0; margin: 5px 0 0 0; font-size: 14px;'>Revenue recognition, cash, receivables, inventory</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Go to ACC 310", key="btn_acc310", use_container_width=True):
                st.session_state.selected_page = "ACC 310 - Intermediate I"
                st.rerun()
            
            st.write("")
            
            # ACC 402 Box
            st.markdown("""
                <div style='background-color: #002E5D; padding: 25px; border-radius: 12px; margin-bottom: 20px;'>
                    <h3 style='color: white; margin: 0;'>📕 ACC 402</h3>
                    <p style='color: white; margin: 10px 0 0 0;'><strong>Cost Accounting</strong></p>
                    <p style='color: #B0B0B0; margin: 5px 0 0 0; font-size: 14px;'>Job costing, process costing, activity-based costing</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Go to ACC 402", key="btn_acc402", use_container_width=True):
                st.session_state.selected_page = "ACC 402 - Cost Accounting"
                st.rerun()
        
        st.write("---")
        st.write("### 🎯 Quick Stats")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Formulas", "25+")
        col2.metric("Classes Covered", "4")
        col3.metric("Calculators", "5+")

    # --- PAGE 2: ACC 200 ---
    elif page == "ACC 200 - Intro":
        # Back to Home button
        if st.button("← Back to Home", key="back_200"):
            st.session_state.selected_page = "🏠 Home"
            st.rerun()
        
        st.title("📘 ACC 200 - Introduction to Accounting")
        st.write("### Key Formulas & Concepts")
        
        # Create expandable sections for each topic
        with st.expander("🔵 Accounting Equation", expanded=True):
            st.write("**Assets = Liabilities + Equity**")
            st.write("*The fundamental equation of accounting*")
            st.code("Example: $100,000 = $40,000 + $60,000", language=None)
        
        with st.expander("🔵 Net Income"):
            st.write("**Net Income = Revenues - Expenses**")
            st.write("*Measures profitability for a period*")
            st.code("Example: $50,000 - $30,000 = $20,000 Net Income", language=None)
        
        with st.expander("🔵 Current Ratio"):
            st.write("**Current Ratio = Current Assets / Current Liabilities**")
            st.write("*Measures short-term liquidity*")
            st.write("- Ratio > 1.0 means you can cover short-term debts")
            st.code("Example: $80,000 / $40,000 = 2.0", language=None)
        
        with st.expander("🔵 Debt-to-Equity Ratio"):
            st.write("**Debt-to-Equity = Total Liabilities / Total Equity**")
            st.write("*Measures financial leverage*")
            st.code("Example: $60,000 / $40,000 = 1.5", language=None)

    # --- PAGE 3: ACC 310 ---
    elif page == "ACC 310 - Intermediate I":
        # Back to Home button
        if st.button("← Back to Home", key="back_310"):
            st.session_state.selected_page = "🏠 Home"
            st.rerun()
        
        st.title("📗 ACC 310 - Intermediate Accounting I")
        st.write("### Key Formulas & Concepts")
        
        with st.expander("🟢 Accounts Receivable (Net)", expanded=True):
            st.write("**Net A/R = Gross A/R - Allowance for Doubtful Accounts**")
            st.write("*The amount you actually expect to collect*")
            st.code("Example: $100,000 - $5,000 = $95,000", language=None)
        
        with st.expander("🟢 Bad Debt Expense (Percentage of Sales)"):
            st.write("**Bad Debt Expense = Credit Sales × Estimated %**")
            st.write("*Income statement approach*")
            st.code("Example: $500,000 × 2% = $10,000", language=None)
        
        with st.expander("🟢 Inventory - FIFO"):
            st.write("**FIFO (First-In, First-Out)**")
            st.write("*Assumes oldest inventory is sold first*")
            st.write("- Used in rising price environments")
            st.write("- Results in lower COGS, higher Net Income")
        
        with st.expander("🟢 Inventory - LIFO"):
            st.write("**LIFO (Last-In, First-Out)**")
            st.write("*Assumes newest inventory is sold first*")
            st.write("- Results in higher COGS, lower Net Income")
            st.write("- Better matches current costs with revenue")
        
        with st.expander("🟢 Cost of Goods Sold"):
            st.write("**COGS = Beginning Inventory + Purchases - Ending Inventory**")
            st.code("Example: $20,000 + $100,000 - $25,000 = $95,000", language=None)

    # --- PAGE 4: ACC 401 ---
    elif page == "ACC 401 - Intermediate II":
        # Back to Home button
        if st.button("← Back to Home", key="back_401"):
            st.session_state.selected_page = "🏠 Home"
            st.rerun()
        
        st.title("📙 ACC 401 - Intermediate Accounting II")
        st.write("### Key Formulas & Concepts")
        
        with st.expander("🟡 Depreciation - Straight Line", expanded=True):
            st.write("**Annual Depreciation = (Cost - Salvage Value) / Useful Life**")
            st.write("*Spreads cost evenly over asset's life*")
            st.code("Example: ($100,000 - $10,000) / 10 years = $9,000/year", language=None)
        
        with st.expander("🟡 Depreciation - Double Declining Balance"):
            st.write("**DDB Rate = (2 / Useful Life) × Book Value**")
            st.write("*Accelerated depreciation method*")
            st.code("Example: (2 / 10) × $100,000 = $20,000 Year 1", language=None)
        
        with st.expander("🟡 Bond Issue Price"):
            st.write("**Price = PV of Principal + PV of Interest Payments**")
            st.write("*Uses present value calculations*")
            st.write("- Discount: Market rate > Stated rate")
            st.write("- Premium: Market rate < Stated rate")
        
        with st.expander("🟡 Interest Expense (Bonds)"):
            st.write("**Interest Expense = Carrying Value × Market Rate**")
            st.write("*For bonds issued at discount/premium*")
            st.code("Example: $95,000 × 6% = $5,700", language=None)
        
        with st.expander("🟡 Lease Liability"):
            st.write("**Lease Liability = PV of Future Lease Payments**")
            st.write("*At inception of lease*")

    # --- PAGE 5: ACC 402 ---
    elif page == "ACC 402 - Cost Accounting":
        # Back to Home button
        if st.button("← Back to Home", key="back_402"):
            st.session_state.selected_page = "🏠 Home"
            st.rerun()
        
        st.title("📕 ACC 402 - Cost Accounting")
        st.write("### Key Formulas & Concepts")
        
        with st.expander("🔴 Contribution Margin", expanded=True):
            st.write("**Contribution Margin = Sales - Variable Costs**")
            st.write("*Amount available to cover fixed costs and profit*")
            st.code("Example: $100,000 - $60,000 = $40,000", language=None)
        
        with st.expander("🔴 Contribution Margin Ratio"):
            st.write("**CM Ratio = Contribution Margin / Sales**")
            st.write("*Percentage of each sales dollar available for fixed costs*")
            st.code("Example: $40,000 / $100,000 = 40%", language=None)
        
        with st.expander("🔴 Break-Even Point (Units)"):
            st.write("**BEP (Units) = Fixed Costs / CM per Unit**")
            st.write("*Number of units needed to cover all costs*")
            st.code("Example: $30,000 / $15 = 2,000 units", language=None)
        
        with st.expander("🔴 Break-Even Point (Dollars)"):
            st.write("**BEP ($) = Fixed Costs / CM Ratio**")
            st.write("*Sales dollars needed to break even*")
            st.code("Example: $30,000 / 0.40 = $75,000", language=None)
        
        with st.expander("🔴 Target Profit (Units)"):
            st.write("**Units Needed = (Fixed Costs + Target Profit) / CM per Unit**")
            st.code("Example: ($30,000 + $20,000) / $15 = 3,333 units", language=None)
        
        with st.expander("🔴 Overhead Rate"):
            st.write("**Predetermined OH Rate = Estimated Overhead / Estimated Activity**")
            st.write("*Used to apply overhead to jobs*")
            st.code("Example: $100,000 / 20,000 hours = $5/hour", language=None)

    # --- PAGE 6: CALCULATORS ---
    elif page == "🧮 Calculators":
        # Back to Home button
        if st.button("← Back to Home", key="back_calc"):
            st.session_state.selected_page = "🏠 Home"
            st.rerun()
        
        st.title("🧮 Quick Calculators")
        
        calc_type = st.selectbox("Choose a Calculator:", [
            "Current Ratio",
            "Return on Equity (ROE)",
            "Break-Even Point",
            "Straight-Line Depreciation"
        ])
        
        if calc_type == "Current Ratio":
            st.write("### Current Ratio Calculator")
            st.write("**Formula:** Current Assets / Current Liabilities")
            
            assets = st.number_input("Current Assets ($)", min_value=0.0, value=100000.0)
            liabilities = st.number_input("Current Liabilities ($)", min_value=0.01, value=50000.0)
            
            if st.button("Calculate Current Ratio"):
                ratio = assets / liabilities
                st.success(f"✅ Current Ratio: **{ratio:.2f}**")
                if ratio >= 2.0:
                    st.info("Strong liquidity position")
                elif ratio >= 1.0:
                    st.info("Adequate liquidity")
                else:
                    st.warning("Potential liquidity concerns")
        
        elif calc_type == "Return on Equity (ROE)":
            st.write("### ROE Calculator")
            st.write("**Formula:** (Net Income / Shareholder's Equity) × 100")
            
            ni = st.number_input("Net Income ($)", value=50000.0)
            equity = st.number_input("Shareholder's Equity ($)", min_value=0.01, value=250000.0)
            
            if st.button("Calculate ROE"):
                roe = (ni / equity) * 100
                st.success(f"✅ ROE: **{roe:.2f}%**")
        
        elif calc_type == "Break-Even Point":
            st.write("### Break-Even Calculator")
            st.write("**Formula:** Fixed Costs / (Price - Variable Cost per Unit)")
            
            price = st.number_input("Price per Unit ($)", value=50.0, min_value=0.01)
            vc = st.number_input("Variable Cost per Unit ($)", value=30.0, min_value=0.0)
            fc = st.number_input("Total Fixed Costs ($)", value=5000.0, min_value=0.0)
            
            if st.button("Calculate Break-Even"):
                if price > vc:
                    bep_units = fc / (price - vc)
                    bep_dollars = bep_units * price
                    st.success(f"✅ Break-Even Point: **{bep_units:.0f} units** or **${bep_dollars:,.0f}**")
                    
                    # Show visualization
                    units = np.linspace(0, bep_units * 2, 100)
                    revenue = units * price
                    costs = fc + (units * vc)
                    
                    chart_data = pd.DataFrame({
                        "Units": units,
                        "Revenue": revenue,
                        "Total Costs": costs
                    })
                    st.line_chart(chart_data, x="Units", y=["Revenue", "Total Costs"])
                else:
                    st.error("Price must be greater than Variable Cost!")
        
        elif calc_type == "Straight-Line Depreciation":
            st.write("### Straight-Line Depreciation Calculator")
            st.write("**Formula:** (Cost - Salvage Value) / Useful Life")
            
            cost = st.number_input("Asset Cost ($)", value=100000.0, min_value=0.0)
            salvage = st.number_input("Salvage Value ($)", value=10000.0, min_value=0.0)
            life = st.number_input("Useful Life (years)", value=10, min_value=1)
            
            if st.button("Calculate Depreciation"):
                annual_dep = (cost - salvage) / life
                st.success(f"✅ Annual Depreciation: **${annual_dep:,.2f}**")
                st.info(f"Total Depreciable Amount: ${cost - salvage:,.2f}")
