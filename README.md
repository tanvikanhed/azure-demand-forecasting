# Azure Demand Forecasting & Customer Growth Analysis

This repository contains the end-to-end project on **Azure Compute and Storage Demand Forecasting** and **Customer Growth Analysis**, covering all milestones (M1 to M4). The project includes data preparation, exploratory analysis, feature engineering, model development, deployment, and dashboard visualization.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Milestones](#milestones)
   - [Milestone 1 (M1) – Data Cleaning & EDA](#milestone-1-m1---data-cleaning--eda)
   - [Milestone 2 (M2) – Feature Engineering & Model Preparation](#milestone-2-m2---feature-engineering--model-preparation)
   - [Milestone 3 (M3) – Demand Forecasting Model](#milestone-3-m3---demand-forecasting-model)
   - [Milestone 4 (M4) – Dashboard & Deployment](#milestone-4-m4---dashboard--deployment)
3. [Project Structure](#project-structure)
4. [Deployment & Links](#deployment--links)
5. [Technologies Used](#technologies-used)
6. [License](#license)

---

## Project Overview
This project aims to analyze Azure Compute and Storage demand data to:  
- Forecast future demand at region and product level  
- Model customer growth patterns  
- Build an interactive dashboard for visualization  
- Automate deployment with real-time monitoring  

---

## Milestones

### Milestone 1 (M1) - Data Cleaning & EDA
- Collected Azure Compute & Storage demand dataset  
- Performed **data cleaning**: removed nulls, duplicates, invalid rows  
- Exploratory Data Analysis (EDA):  
  - Trend analysis  
  - Region-wise demand patterns  
  - Seasonal patterns in usage  
- Output: Cleaned dataset ready for modeling

**Files/Code:**  
- `M1_Data_Cleaning.ipynb`  
- `EDA_Analysis.ipynb`  

---

### Milestone 2 (M2) - Feature Engineering & Model Preparation
- Engineered features for forecasting model:
  - Lag features  
  - Moving averages  
  - Time-based features (day, month, quarter)  
- Prepared model-ready datasets  
- Validated features and handled multicollinearity  

**Files/Code:**  
- `M2_Feature_Engineering.ipynb`  
- `Model_Preparation.ipynb`  

---

### Milestone 3 (M3) - Demand Forecasting Model
- Built and trained forecasting model:  
  - Algorithms used: **Prophet / ARIMA / LSTM (as applicable)**  
  - Trained on historical demand data  
  - Evaluated model using RMSE, MAPE metrics  
- Generated forecasts for future periods  
- Saved model for deployment

**Files/Code:**  
- `M3_Model_Training.ipynb`  
- `Forecasting_Model.pkl`  

---

### Milestone 4 (M4) - Dashboard & Deployment
- Developed interactive **Power BI / Tableau** dashboard:  
  - Region-wise and product-wise demand trends  
  - Forecast visualization  
  - Key metrics and KPIs  
- Integrated automated model deployment:  
  - Scheduled forecasting using **Python scheduler / Task Scheduler**  
  - Real-time monitoring for errors and prediction logs  
- Automated CSV export and dashboard updates  

**Files/Code:**  
- `M4_Dashboard_Development.ipynb`  
- `Dashboard.pbix`  

---

## Project Structure
project-root/
│
├─ M1_Data_Cleaning.ipynb
├─ EDA_Analysis.ipynb
├─ M2_Feature_Engineering.ipynb
├─ Model_Preparation.ipynb
├─ M3_Model_Training.ipynb
├─ Forecasting_Model.pkl
├─ M4_Dashboard_Development.ipynb
├─ Dashboard.pbix
├─ README.md
└─ requirements.txt

## Deployment & Links
- **Deployed Dashboard / Public Link:** https://azure-demand-forecasting-edw4al6ddysfglws5b8s2a.streamlit.app/  
- **Model Download Link (Optional):** https://github.com/tanvikanhed/azure-demand-forecasting/blob/main/model%20(1).pkl

## Technologies Used
- Python (pandas, numpy, scikit-learn, statsmodels, prophet, matplotlib, seaborn)  
- Power BI / Tableau  
- CSV, Pickle for data/model storage  
- Scheduler / Automation scripts for deployment  

## References
- Azure public datasets
- XGBoost documentation: https://xgboost.readthedocs.io/
- Python libraries: pandas, numpy, scikit-learn

  ## Notes
- Download `model.pkl` from the link above to use the trained XGBoost model.
- Run the notebooks in order: M1 → M2 → M3 → M4.
- For dashboard visualization, open `M4_Dashboard_Development.ipynb` or Power BI file `Dashboard.pbix`.
- All scripts were tested in Python 3.10 and require the libraries listed in `requirements.txt`.

  ## License
This project is licensed under the MIT License.

----

