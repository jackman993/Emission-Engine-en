"""
Carbon Emission Calculator
Streamlit App
"""
import streamlit as st

st.set_page_config(
    page_title="Carbon Emission Calculator",
    page_icon="🌍",
    layout="wide"
)

# Redirect to main calculator
st.switch_page("pages/Calculator.py")
