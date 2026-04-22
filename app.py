import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


# Load model

st.title("AI-Based Manufacturing Efficiency Dashboard")

st.sidebar.header("Input Parameters")

temperature = st.sidebar.slider("Temperature (°C)", 20.0, 100.0, 50.0)
vibration = st.sidebar.slider("Vibration (Hz)", 0.1, 5.0, 1.0)
power = st.sidebar.slider("Power Consumption (kW)", 10.0, 500.0, 100.0)
latency = st.sidebar.slider("Network Latency (ms)", 1.0, 100.0, 10.0)
packet_loss = st.sidebar.slider("Packet Loss (%)", 0.0, 10.0, 1.0)
defect_rate = st.sidebar.slider("Defect Rate (%)", 0.0, 20.0, 2.0)
production_speed = st.sidebar.slider("Production Speed", 10.0, 500.0, 100.0)
maintenance_score = st.sidebar.slider("Maintenance Score", 0.0, 1.0, 0.5)
error_rate = st.sidebar.slider("Error Rate (%)", 0.0, 10.0, 1.0)

# Operation Mode (ADD THIS)
operation_mode = st.sidebar.selectbox("Operation Mode", ["Active", "Idle", "Maintenance"])

# Encoding (IMPORTANT)
if operation_mode == "Active":
    idle = 0
    maintenance = 0
elif operation_mode == "Idle":
    idle = 1
    maintenance = 0
else:
    idle = 0
    maintenance = 1

# Feature Engineering
energy_per_unit = power / production_speed
error_per_output = error_rate / production_speed
network_quality = (100 - packet_loss) / latency
sensor_stability = temperature / vibration

input_data = np.array([[temperature, vibration, power, latency, packet_loss,
                        defect_rate, production_speed, maintenance_score,
                        error_rate, idle, maintenance,
                        energy_per_unit, error_per_output,
                        network_quality, sensor_stability]])

input_scaled = scaler.transform(input_data)

prediction = model.predict(input_scaled)
confidence = np.max(model.predict_proba(input_scaled))

labels = {0: "Low", 1: "Medium", 2: "High"}

st.subheader("Prediction Result")
st.write(f"Efficiency Status: **{labels[prediction[0]]}**")
st.write(f"Confidence: **{confidence:.2f}**")
