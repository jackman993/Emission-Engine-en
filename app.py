"""
Carbon Emission Calculator
Streamlit App
"""
import streamlit as st

st.set_page_config(
    page_title="Carbon Emission Calculator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Show welcome page - Streamlit will automatically show pages/Calculator.py in sidebar
st.title("🌍 Carbon Emission Calculator")
st.divider()

st.info("💡 **Tip**: Use the sidebar navigation menu to access the Calculator page.")

st.markdown("""
### Welcome to the Carbon Emission Calculator

This tool helps you calculate carbon emissions based on:
- Electricity consumption
- Region-specific emission factors
- Multiple calculation methods

**Get Started**: Click on "Calculator" in the sidebar navigation menu (☰) to begin.
""")
