# Azure Demand Forecasting & Customer Growth Analysis
##  Project Overview
This project analyzes Azure Compute and Storage demand data to prepare it for forecasting and customer growth modeling.

**The project is divided into milestones:**
- **Milestone 1:** Data Cleaning, Validation, and Exploratory Data Analysis (EDA)
- **Milestone 2:** Feature Engineering and Model-Ready Dataset Preparation
- **Milestone 3 (Upcoming):** Demand Forecasting Model & Deployment
  
##  Dataset Summary
- **Time Span:** January 2023 – December 2024 (Daily data)
  
**Regions:**
- East US
- West Europe
- Central India
- Southeast Asia
  
**Services:**
- Compute
- Storage
 
- **Granularity:** Daily region-service level records
##  Original Features
- `timestamp` – Daily date
- `region` – Azure region
- `service_type` – Compute / Storage
- `demand_units` – Workload demand (Target Variable)
- `capacity_allocated` – Provisioned capacity
- `cost_usd` – Operational cost
- `availability_pct` – SLA availability
- `customer_growth_rate` – Business growth factor
- `enterprise_it_spending_index` – Economic indicator
  
## Milestone 1 – Data Cleaning & EDA
###  Data Preparation
- Converted `timestamp` to datetime
- Sorted data chronologically
- Standardized region and service values
- Removed duplicates
- Handled ~3% missing values using:
  - Interpolation
  - Forward fill
  - Logical recalculation
- Performed validation checks
  
###  Exploratory Data Analysis
- Monthly average demand trend
- Region-wise demand comparison
- Service type demand comparison
- Correlation matrix for numerical features
- Trend and distribution visualization
  
Cleaned dataset saved as:
`data/azure_ts_24m_clean.csv`

## Milestone 2 – Feature Engineering

**Milestone 2 prepares the dataset for machine learning and forecasting.**

###  Time-Based Features
Extracted from `timestamp`:
- `year`
- `month`
- `day`
- `day_of_week`
- `is_weekend`
  
###  Lag Features (Time Dependency)
Created region-service group-based lag features:
- `lag_1` – Previous day demand
- `lag_7` – Previous week demand
  
###  Rolling Feature
- `rolling_mean_7` – 7-day moving average demand
  
###  Demand Spike Detection
Created `demand_spike` column:
- Value = 1 if demand > (mean + 1.5 × std)
- Value = 0 otherwise
Used to identify unusual demand surges.

###  Encoding & Final Processing
- One-hot encoded:
  - `region`
  - `service_type`
- Removed non-numeric columns
- Converted boolean columns to integers
- Removed lag-induced null rows
- Verified no missing values remain
  
##  Final Model-Ready Dataset
- Rows: 1048
- Columns: 18
- Fully numeric
- No missing values
- Ready for regression modeling
Saved as:
`data/Milestone2_ModelReady.csv`

##  Repository Structure
```
Azure-Demand-Forecasting/
│
├── data/
│   ├── azure_demand_dataset.csv
│   ├── azure_ts_24m_clean.csv
│   └── Milestone2_ModelReady.csv
│
├── notebooks/
│   ├── AzureFile.ipynb
│   └── Azure_milestone2.ipynb
│
├── README.md
└── MIT license.txt
```
##  Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
  
##  Next Steps (Milestone 3)
- Train demand forecasting regression model
- Evaluate performance metrics
- Build prediction pipeline
- Deploy forecasting solution
  
##  Objective
To build a scalable Azure demand forecasting system that supports capacity planning, cost optimization, and customer growth analysis.
