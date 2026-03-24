# Azure Demand Forecasting & Customer Growth Analysis

This project focuses on forecasting Azure Compute and Storage demand using Machine Learning. It covers the complete pipeline from data preprocessing to model deployment and visualization.

---

## Project Overview

The goal of this project is to:
- Predict future demand using historical data
- Analyze demand trends across regions and services
- Build a complete ML pipeline with batch and real-time predictions
- Visualize predictions for decision-making

---

## Milestones

### Milestone 1 (M1) – Data Cleaning & EDA
- Cleaned raw dataset (handled null values, duplicates)
- Performed Exploratory Data Analysis (EDA)
- Identified trends and patterns in demand

---

### Milestone 2 (M2) – Feature Engineering
- Created model-ready dataset
- Added time-based and derived features
- Final dataset: `Milestone2_ModelReady.csv`

---

### Milestone 3 (M3) – Model Development
- Trained **XGBoost Regressor model**
- Performed train-test split
- Evaluated model using:
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
- Generated predictions
- Saved trained model as `model.pkl`

---

### Milestone 4 (M4) – Deployment & Visualization

#### 🔹 Batch Prediction Pipeline
- Input: `new_data.csv`
- Output: `forecast_output.csv`
- Generates predictions for multiple records

#### 🔹 FastAPI (Real-Time Prediction)
- Built API endpoint:
- POST /predict
-  Takes input data and returns predicted demand
- Enables real-time forecasting

#### 🔹 Streamlit Dashboard
- Built interactive dashboard using Streamlit
- Visualizations include:
- Actual vs Predicted demand (time-series)
- Demand trends
- Region/service-based analysis

---

## Data Flow
new_data.csv

↓

Batch Prediction Script / FastAPI API

↓

forecast_output.csv

↓

Streamlit Dashboard

↓

Decision Making


---

## Project Structure
project-root/
│

├─ M1_Data_Cleaning.ipynb

├─ M2_Feature_Engineering.ipynb

├─ M3_Model_Training.ipynb

├─ model.pkl

├─ forecast_output.csv

├─ app.py # FastAPI app

├─ streamlit_app.py # Streamlit dashboard

├─ README.md

└─ requirements.txt



---

## Model Download

## Deployment & Links
- **Deployed Dashboard:** https://azure-demand-forecasting-edw4al6ddysfglws5b8s2a.streamlit.app/  
- **Model Download Link :** https://github.com/tanvikanhed/azure-demand-forecasting/blob/main/model%20(1).pkl
---

## Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- FastAPI (for API)
- Streamlit (for dashboard)
- Pickle (for model saving)

---

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run FastAPI server
uvicorn app:app --reload

### 3. Run Streamlit dashboard
streamlit run streamlit_app.py


---

## Key Concepts

- **Batch Prediction:** Processes multiple inputs from CSV at once  
- **Real-Time Prediction:** API-based prediction using FastAPI  
- **Model Persistence:** Saved using `.pkl` for reuse  
- **Visualization:** Built using Streamlit  

---

