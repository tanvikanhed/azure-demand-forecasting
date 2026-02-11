# Azure Demand Forecasting & Customer Growth Analysis

## 📌 Project Overview
This project analyzes Azure service demand data over a 12–24 month period across multiple regions.  
The objective is to clean, validate, and prepare the dataset for time-series forecasting and enterprise capacity planning.

This is **Milestone 1** of the project, focusing on data collection, preprocessing, and visualization.
## Dataset Description
The dataset contains the following features:

- timestamp – Date of record (daily granularity)
- region – Azure region (US-East, US-West, India-South)
- service_type – Compute or Storage
- usage_units – Resource demand (cores / GB)
- capacity_allocated – Provisioned infrastructure capacity
- cost_usd – Cost associated with usage
- availability_pct – Service availability percentage
- customer_growth_rate – Monthly growth rate of active customers (external factor)

Time range: 12–24 months  
Total records: ~3000 rows  

## Data Cleaning & Preparation Steps
The following preprocessing steps were performed:

- Standardized column names
- Converted `timestamp` to datetime format
- Sorted dataset for time-series consistency
- Removed duplicate records
- Handled missing values:
  - Interpolated `usage_units`
  - Recomputed or filled `cost_usd` where necessary
  - Forward-filled `availability_pct`
  - Interpolated `customer_growth_rate`
  - Validated dataset consistency and structure
  - Created clean time-series visualizations
    
## Visualizations
- Region-wise usage trend over time
- Time-series demand trend analysis
- Capacity vs Usage comparison
  
## Tools & Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Google Colab
  
##  Business Relevance
This dataset enables:

- Demand forecasting
- Capacity planning optimization
- Cost trend analysis
- Understanding the impact of customer growth on infrastructure demand
  
## How to Run the Project
1. Clone the repository  
2. Open the notebook in Jupyter or Google Colab  
3. Run all cells sequentially
   
## Project Status
Milestone 1 – Data Collection & Preparation – Completed  
Ready for Forecasting Model Development (Milestone 2)
