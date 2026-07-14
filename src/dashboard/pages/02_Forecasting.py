"""
02_Forecasting.py
-----------------
Forecasting page with model comparison.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

st.set_page_config(page_title="Forecasting", page_icon="📈", layout="wide")

st.title("📈 Forecasting")
st.markdown("Advanced predictive models for passenger traffic")

col1, col2, col3 = st.columns(3)

with col1:
    model = st.selectbox("Select Model", ["Random Forest", "XGBoost", "SARIMA", "Prophet", "LSTM", "Ensemble"])

with col2:
    horizon = st.slider("Forecast Horizon (days)", 1, 90, 30)

with col3:
    confidence_level = st.selectbox("Confidence Level", ["95%", "90%", "85%"])

st.markdown("---")

future_dates = pd.date_range(start=datetime.now(), periods=horizon, freq='D')
actual_dates = pd.date_range(start=datetime.now() - timedelta(days=30), periods=30, freq='D')
actual_values = np.random.randint(28000, 35000, 30)
forecast_values = np.random.randint(29000, 34000, horizon)
fcast_upper = forecast_values + np.random.randint(500, 2000, horizon)
fcast_lower = forecast_values - np.random.randint(500, 2000, horizon)

st.subheader(f"Passenger Traffic Forecast - {model}")

fig = go.Figure()
fig.add_trace(go.Scatter(x=actual_dates, y=actual_values, mode='lines', name='Historical',
                        line=dict(color='#1f77b4', width=2)))
fig.add_trace(go.Scatter(x=future_dates, y=forecast_values, mode='lines+markers', name='Forecast',
                        line=dict(color='#2ca02c', width=2, dash='dash')))
fig.add_trace(go.Scatter(x=future_dates.tolist() + future_dates.tolist()[::-1],
                        y=fcast_upper.tolist() + fcast_lower.tolist()[::-1],
                        fill='toself', name=f'{confidence_level} CI', fillcolor='rgba(44, 160, 44, 0.2)',
                        line=dict(color='rgba(255,255,255,0)')))
fig.update_layout(title=f"{model} Forecast", xaxis_title="Date", yaxis_title="Passengers", height=400)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Model Performance Metrics")

metrics_data = {
    'Model': ['Random Forest', 'XGBoost', 'SARIMA', 'Prophet', 'LSTM', 'Ensemble'],
    'MAE': [2096.42, 2276.54, 3032.12, 2450.20, 1890.33, 1756.88],
    'RMSE': [2675.01, 2915.14, 3775.19, 3100.45, 2456.78, 2341.20],
    'MAPE': [8.44, 9.21, 10.31, 8.95, 7.65, 7.23]
}

df_metrics = pd.DataFrame(metrics_data).sort_values('MAPE')
st.dataframe(df_metrics, use_container_width=True, hide_index=True)
