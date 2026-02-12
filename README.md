# Azure Demand Forecasting & Customer Growth Analysis  

## Project Overview  
This project analyzes Azure Compute and Storage demand data to prepare it for forecasting and customer growth modeling.  
Milestone 1 focuses on data cleaning, validation, and exploratory data analysis (EDA).

## Dataset Summary  

**Time Span:** Jan 2023 – Dec 2024 (Daily data)  
**Regions:** East US, West Europe, Central India, Southeast Asia  
**Services:** Compute, Storage  

### Features
- `timestamp` – Daily date  
- `region` – Azure region  
- `service_type` – Compute / Storage  
- `demand_units` – Workload demand  
- `capacity_allocated` – Provisioned capacity  
- `cost_usd` – Operational cost  
- `availability_pct` – SLA availability  
- `customer_growth_rate` – Business growth factor  
- `enterprise_it_spending_index` – Economic indicator
  
## Data Preparation  
- Converted timestamps and sorted chronologically  
- Standardized region and service values  
- Removed duplicates  
- Handled ~3% missing values using interpolation, recalculation, and forward fill  
- Performed validation checks  

## EDA Performed  
- Monthly Average Demand Trend  
- Region-wise Demand Trend  
- Service Type Comparison  

## Files  
- `azure_demand_dataset.csv` – Raw dataset  
- `azure_demand_cleaned_v2.csv` – Cleaned dataset  

