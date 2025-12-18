"""
Carbon Emission Calculator
Main calculation page with region selection
"""
import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path (now Calculator.py is in pages/, so parent.parent gets root)
sys.path.insert(0, str(Path(__file__).parent.parent))

from emission_calc import Inputs, estimate, GRID_EMISSION_FACTORS

st.set_page_config(
    page_title="Calculator",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Carbon Emission Calculator")

st.divider()

# === Region Selection ===
st.subheader("📍 Region Selection")

region_names = {
    "TW": "🇹🇼 Taiwan",
    "US": "🇺🇸 United States",
    "EU": "🇪🇺 European Union",
    "CN": "🇨🇳 China",
    "JP": "🇯🇵 Japan"
}

region = st.selectbox(
    "Select Your Region",
    options=list(region_names.keys()),
    format_func=lambda x: region_names[x],
    help="Different regions have different grid emission factors"
)

grid_ef = GRID_EMISSION_FACTORS[region]
st.info(f"Grid Emission Factor: **{grid_ef} kg CO2/kWh**")

st.divider()

# === Input Section ===
st.subheader("📊 Input Data")

tab1, tab2 = st.tabs(["Quick Mode", "Detailed Mode"])

with tab1:
    st.write("**Quick Estimation (Monthly Bill)**")
    
    monthly_bill = st.number_input(
        "Monthly Electricity Bill (USD/NTD/EUR)",
        min_value=0,
        value=5000,
        step=500
    )
    
    price_per_kwh = st.number_input(
        "Electricity Price per kWh",
        min_value=0.0,
        value=0.12,
        step=0.01,
        help="Typical: US $0.12, TW NT$4.4, EU €0.25"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        cars = st.number_input("Number of Cars", min_value=0, value=5)
    
    with col2:
        motorcycles = st.number_input("Number of Motorcycles", min_value=0, value=10)
    
    if st.button("Calculate (Quick)", type="primary", use_container_width=True):
        inputs = Inputs(
            region=region,
            mode="quick",
            monthly_bill_ntd=float(monthly_bill),
            price_per_kwh_ntd=float(price_per_kwh),
            car_count=float(cars),
            motorcycles=float(motorcycles),
            use_rule_of_thumb=True
        )
        
        result = estimate(inputs)
        st.session_state.result = result
        st.session_state.calculation_done = True

with tab2:
    st.write("**Detailed Estimation**")
    
    annual_kwh = st.number_input(
        "Annual Electricity Consumption (kWh)",
        min_value=0,
        value=500000,
        step=10000
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        gasoline = st.number_input(
            "Annual Gasoline (Liters)",
            min_value=0,
            value=15000,
            step=1000
        )
        
        refrigerant = st.number_input(
            "Refrigerant Leakage (kg/year)",
            min_value=0.0,
            value=5.0,
            step=0.5
        )
    
    with col2:
        diesel = st.number_input(
            "Annual Diesel (Liters)",
            min_value=0,
            value=5000,
            step=1000
        )
        
        gwp = st.number_input(
            "Refrigerant GWP",
            min_value=0,
            value=1430,
            step=100,
            help="Common: R-134a (1430), R-410A (2088), R-32 (675)"
        )
    
    include_scope3 = st.checkbox("Include Scope 3 (Water & Waste)", value=True)
    
    if include_scope3:
        col1, col2 = st.columns(2)
        with col1:
            water = st.number_input("Water (m³/year)", min_value=0, value=2000, step=100)
        with col2:
            waste = st.number_input("Waste (tons/year)", min_value=0, value=50, step=5)
    else:
        water = 0
        waste = 0
    
    if st.button("Calculate (Detailed)", type="primary", use_container_width=True):
        inputs = Inputs(
            region=region,
            mode="detail",
            annual_kwh=float(annual_kwh),
            gasoline_liters_year=float(gasoline),
            diesel_liters_year=float(diesel),
            refrigerant_leak_kg=float(refrigerant),
            refrigerant_gwp=float(gwp),
            include_scope3=include_scope3,
            water_m3_year=float(water),
            waste_ton_year=float(waste)
        )
        
        result = estimate(inputs)
        st.session_state.result = result
        st.session_state.calculation_done = True

st.divider()

# === Results Section ===
if st.session_state.get("calculation_done"):
    st.subheader("📈 Results")
    
    result = st.session_state.result
    
    # Summary Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Scope 2 (Electricity)",
            f"{result['Scope2_Electricity']} tCO2e",
            delta=f"{result['Share_Percent']['Electricity']}%"
        )
    
    with col2:
        st.metric(
            "Scope 1 (Vehicles)",
            f"{result['Scope1_Vehicles']} tCO2e",
            delta=f"{result['Share_Percent']['Vehicles']}%"
        )
    
    with col3:
        st.metric(
            "Scope 1 (Refrigerant)",
            f"{result['Scope1_Refrigerant']} tCO2e",
            delta=f"{result['Share_Percent']['Refrigerant']}%"
        )
    
    with col4:
        st.metric(
            "Total Emissions",
            f"{result['Total_S1S2']} tCO2e"
        )
    
    # Detailed Breakdown
    st.divider()
    
    st.subheader("🔍 Detailed Breakdown")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Emission Sources:**")
        st.write(f"- Scope 2 (Electricity): {result['Scope2_Electricity']} tCO2e")
        st.write(f"- Scope 1 (Vehicles): {result['Scope1_Vehicles']} tCO2e")
        st.write(f"- Scope 1 (Refrigerant): {result['Scope1_Refrigerant']} tCO2e")
        st.write(f"- Scope 1 Total: {result['Scope1_Total']} tCO2e")
        st.write(f"- **Total (S1+S2): {result['Total_S1S2']} tCO2e**")
        
        if result['Scope3_Minor'] > 0:
            st.write(f"- Scope 3 (Minor): {result['Scope3_Minor']} tCO2e")
            st.write(f"- **Total (with S3): {result['Total_With_S3']} tCO2e**")
    
    with col2:
        st.write("**Calculation Details:**")
        st.write(f"- Region: {region_names[result['Region']]}")
        st.write(f"- Grid Emission Factor: {result['Grid_EF']} kg CO2/kWh")
        st.write(f"- Electricity Share: {result['Share_Percent']['Electricity']}%")
        st.write(f"- Vehicles Share: {result['Share_Percent']['Vehicles']}%")
        st.write(f"- Refrigerant Share: {result['Share_Percent']['Refrigerant']}%")
    
    # Download Button
    st.divider()
    
    report = f"""Carbon Emission Calculation Report
===================================

Region: {region_names[result['Region']]}
Grid Emission Factor: {result['Grid_EF']} kg CO2/kWh

RESULTS
-------
Scope 2 (Electricity): {result['Scope2_Electricity']} tCO2e ({result['Share_Percent']['Electricity']}%)
Scope 1 (Vehicles): {result['Scope1_Vehicles']} tCO2e ({result['Share_Percent']['Vehicles']}%)
Scope 1 (Refrigerant): {result['Scope1_Refrigerant']} tCO2e ({result['Share_Percent']['Refrigerant']}%)
Scope 1 Total: {result['Scope1_Total']} tCO2e

Total Emissions (Scope 1+2): {result['Total_S1S2']} tCO2e
"""
    
    if result['Scope3_Minor'] > 0:
        report += f"Scope 3 (Minor): {result['Scope3_Minor']} tCO2e\n"
        report += f"Total Emissions (with Scope 3): {result['Total_With_S3']} tCO2e\n"
    
    st.download_button(
        "📥 Download Report",
        data=report,
        file_name="carbon_emission_report.txt",
        mime="text/plain",
        use_container_width=True
    )

st.divider()

# === Information Section ===
with st.expander("ℹ️ About Emission Factors"):
    st.write("""
    **Grid Emission Factors by Region:**
    
    | Region | EF (kg CO2/kWh) | Year |
    |--------|----------------|------|
    | Taiwan 🇹🇼 | 0.495 | 2024 |
    | USA 🇺🇸 | 0.386 | 2024 |
    | EU 🇪🇺 | 0.295 | 2024 |
    | China 🇨🇳 | 0.581 | 2024 |
    | Japan 🇯🇵 | 0.441 | 2024 |
    
    **Fuel Emission Factors:**
    - Gasoline: 2.3 kg CO2/L
    - Diesel: 2.6 kg CO2/L
    
    **Scope 3 Coverage:**
    - ✅ Water consumption
    - ✅ Waste disposal
    - ⚠️ Supply chain data not included (unavailable for most SMEs)
    """)
