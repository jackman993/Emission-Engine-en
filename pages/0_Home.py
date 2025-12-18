"""
Home Page
"""
import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

st.title("🌍 Carbon Emission Calculator")
st.divider()

st.markdown("""
### Welcome to the Carbon Emission Calculator

This tool helps you calculate carbon emissions based on:
- Electricity consumption
- Region-specific emission factors
- Multiple calculation methods

**Get Started**: Use the sidebar navigation menu to access the Calculator page.
""")

st.info("💡 **Tip**: If you don't see the sidebar navigation, try refreshing the page or clearing your browser cache.")

