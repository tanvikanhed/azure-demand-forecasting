import streamlit as st
import pandas as pd
import requests

# -------------------------------
# TITLE
# -------------------------------
st.title("Azure Demand Forecast Dashboard")

# -------------------------------
# USER INPUT
# -------------------------------
st.subheader("Enter Input for Prediction")

capacity = st.number_input("Capacity Allocated", value=500)
cost = st.number_input("Cost (USD)", value=100)
availability = st.number_input("Availability %", value=99.0)
growth = st.number_input("Customer Growth Rate", value=0.02)

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("forecast_output.csv")

df['forecast'] = pd.to_numeric(df['forecast'], errors='coerce')

# -------------------------------
# PREDICTION BUTTON
# -------------------------------
if st.button("Get Prediction"):
    
    url = "http://127.0.0.1:8000/predict"
    
    data = {
        "capacity_allocated": capacity,
        "cost_usd": cost,
        "availability_pct": availability,
        "customer_growth_rate": growth
    }

    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        result = response.json()
        forecast_value = result['forecast']
        
        st.success(f"Forecast Demand: {forecast_value}")

        # Save prediction
        st.session_state['new_forecast'] = forecast_value
    else:
        st.error("API Error")

# -------------------------------
# KPI SECTION
# -------------------------------
st.subheader("Key Metrics")

st.metric("Total Demand", round(df['forecast'].sum(), 2))
st.metric("Peak Demand", round(df['forecast'].max(), 2))

# -------------------------------
# HISTORICAL + NEW FORECAST
# -------------------------------
st.subheader("Forecast Trend")

if 'new_forecast' in st.session_state:
    temp_df = df.copy()
    temp_df.loc[len(temp_df)] = {
        'forecast': st.session_state['new_forecast'],
        'region': 'User Input',
        'service_type': 'User Input'
    }
    st.line_chart(temp_df['forecast'])
else:
    st.line_chart(df['forecast'])

# -------------------------------
# REGION-WISE DEMAND
# -------------------------------
st.subheader("Region-wise Demand")

region_data = df.groupby('region')['forecast'].sum()

if 'new_forecast' in st.session_state:
    region_data['User Input'] = st.session_state['new_forecast']

st.bar_chart(region_data)

# -------------------------------
# SERVICE TYPE DEMAND
# -------------------------------
st.subheader("Service Type Demand")

service_data = df.groupby('service_type')['forecast'].sum()

if 'new_forecast' in st.session_state:
    service_data['User Input'] = st.session_state['new_forecast']

st.bar_chart(service_data)

# -------------------------------
# LATEST PREDICTION COMPARISON
# -------------------------------
if 'new_forecast' in st.session_state:
    st.subheader("Latest Prediction vs Average")

    latest_df = pd.DataFrame({
        'Type': ['Average Demand', 'New Prediction'],
        'Value': [df['forecast'].mean(), st.session_state['new_forecast']]
    })

    st.bar_chart(latest_df.set_index('Type'))