"""
Carbon Emission Calculator
Streamlit App - Main Entry Point
"""
import streamlit as st

st.set_page_config(
    page_title="Carbon Emission Calculator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Streamlit will automatically show pages/ directory files in sidebar navigation
# Redirect to Home page if it exists, otherwise show welcome message
try:
    st.switch_page("pages/0_Home")
except:
    # Fallback: show welcome message
    st.title("🌍 Carbon Emission Calculator")
    st.divider()
    
    st.info("💡 **Tip**: Use the sidebar navigation menu (☰) to access pages.")
    
    st.markdown("""
    ### Welcome to the Carbon Emission Calculator
    
    This tool helps you calculate carbon emissions based on:
    - Electricity consumption
    - Region-specific emission factors
    - Multiple calculation methods
    
    **Get Started**: Click on "Calculator" or "Home" in the sidebar navigation menu to begin.
    """)
