"""
01_Overview.py
--------------
Dashboard overview page with real-time KPIs.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

st.set_page_config(page_title="Overview", page_icon="📊", layout="wide")

st.title("📊 Operational Overview")
st.markdown("Real-time KPIs and operational metrics")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Flights Today", "247", "+12")
with col2:
    st.metric("On-Time %", "77.5%", "-2.5%", delta_color="inverse")
with col3:
    st.metric("Passengers", "30.8K", "+5%")
with col4:
    st.metric("Staff Utilization", "89%", "+3%", delta_color="inverse")
with col5:
    st.metric("Queue Time", "7.9 min", "-0.5 min")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Passenger Traffic Trend")
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), periods=30)
    passengers = np.random.randint(28000, 35000, 30)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=passengers, mode='lines+markers', name='Daily Passengers',
                            line=dict(color='#1f77b4', width=2), fill='tozeroy'))
    fig.update_layout(height=400, hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("### Delay Rate Trend")
    delay_rate = np.random.uniform(0.15, 0.35, 30) * 100
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=delay_rate, mode='lines+markers', name='Delay Rate (%)',
                            line=dict(color='#d62728', width=2), fill='tozeroy'))
    fig.update_layout(height=400, hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Operational Status by Department")

status_data = {
    'Department': ['Baggage', 'Check-in', 'Security', 'Gates', 'Boarding', 'Ground'],
    'Status': ['Operational'] * 6,
    'Utilization': [85, 92, 78, 88, 95, 82],
    'Staff': [45, 38, 52, 61, 28, 34],
    'Issues': [0, 1, 0, 0, 3, 1]
}

df_status = pd.DataFrame(status_data)
st.dataframe(df_status, use_container_width=True, hide_index=True)
