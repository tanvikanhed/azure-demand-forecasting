import streamlit as st
import pandas as pd

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
# SIMPLE LOCAL PREDICTION LOGIC
# -------------------------------
if st.button("Get Prediction"):
    
    forecast_value = (
        capacity * 0.3 +
        cost * 0.2 +
        availability * 1.5 +
        growth * 100
    )

    st.success(f"Forecast Demand: {round(forecast_value,2)}")

    st.session_state['new_forecast'] = forecast_value

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("forecast_output.csv")

df['forecast'] = pd.to_numeric(df['forecast'], errors='coerce')

# -------------------------------
# KPI
# -------------------------------
st.subheader("Key Metrics")

st.metric("Total Demand", round(df['forecast'].sum(), 2))
st.metric("Peak Demand", round(df['forecast'].max(), 2))

# -------------------------------
# LINE CHART
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
# REGION
# -------------------------------
st.subheader("Region-wise Demand")

region_data = df.groupby('region')['forecast'].sum()

if 'new_forecast' in st.session_state:
    region_data['User Input'] = st.session_state['new_forecast']

st.bar_chart(region_data)

# -------------------------------
# SERVICE
# -------------------------------
st.subheader("Service Type Demand")

service_data = df.groupby('service_type')['forecast'].sum()

if 'new_forecast' in st.session_state:
    service_data['User Input'] = st.session_state['new_forecast']

st.bar_chart(service_data)
