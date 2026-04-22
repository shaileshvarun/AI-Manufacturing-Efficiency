AI-Based Manufacturing Efficiency Classification
## Project Overview

This project develops an AI-based system to classify manufacturing efficiency using sensor data, 
production metrics, and 6G network parameters. The system predicts whether efficiency is High, Medium, or Low in real time.

## Problem Statement

In smart factories, efficiency can fluctuate due to:

Sensor deviations
Network instability
Quality defects and errors

Traditional dashboards only show past data. This project provides real-time predictive classification to support faster decision-making.

## Dataset Description

The dataset includes:

Machine sensor data (Temperature, Vibration)
Network metrics (Latency, Packet Loss)
Production metrics (Speed, Power Consumption)
Quality indicators (Defect Rate, Error Rate)
### Methodology
1. Data Preprocessing
Datetime conversion
Encoding categorical variables
Feature scaling
2. Feature Engineering

## Created new features such as:

Energy per unit
Error per output
Network quality
Sensor stability
3. Model Development

## Models used:

Logistic Regression
Random Forest (Best performing)
XGBoost
## Model Performance
Model	Accuracy
Logistic Regression	93.57%
Random Forest	99.99%
XGBoost	99.93%
### Key Insights
Error rate and production speed are the most important factors
Network quality significantly impacts efficiency
Feature engineering greatly improves model performance

### Streamlit Dashboard

An interactive dashboard allows users to:

Input machine parameters
Get real-time efficiency prediction
View prediction confidence

## How to Run the Project
1. Install Dependencies
pip install pandas numpy scikit-learn streamlit xgboost
2. Run the App
streamlit run app.py
📂 Project Structure
├── app.py
├── model.pkl
├── scaler.pkl
├── manufacturing_efficiency.ipynb
├── Thales_Group_Manufacturing.csv
├── README.md

 ### Conclusion

This project demonstrates how AI can enable real-time efficiency monitoring in smart manufacturing systems,
helping reduce downtime and improve productivity.

### Author
Shailesh Varun
