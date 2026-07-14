"""
03_Anomalies.py
---------------
Anomaly detection monitoring.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

st.set_page_config(page_title="Anomalies", page_icon="⚠️", layout="wide")

st.title("⚠️ Anomaly Detection")
st.markdown("Real-time detection of operational anomalies")

col1, col2, col3 = st.columns(3)

with col1:
    detection_method = st.selectbox("Detection Method", ["Ensemble", "Isolation Forest", "LOF", "DBSCAN"])

with col2:
    time_range = st.selectbox("Time Range", ["Last 7 days", "Last 30 days", "Last 90 days"])

with col3:
    severity_filter = st.multiselect("Severity Level", ["Critical", "High", "Medium", "Low"],
                                     default=["Critical", "High"])

st.markdown("---")

st.subheader("Anomaly Score Distribution")

normal_scores = np.random.normal(0.3, 0.1, 500)
anomaly_scores = np.random.normal(0.85, 0.08, 50)

fig = go.Figure()
fig.add_trace(go.Histogram(x=normal_scores, name='Normal', marker_color='#2ca02c', opacity=0.7))
fig.add_trace(go.Histogram(x=anomaly_scores, name='Anomaly', marker_color='#d62728', opacity=0.7))
fig.update_layout(title=f"Anomaly Scores - {detection_method}", height=350, barmode='overlay')
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Recent Anomalies")

anomalies_data = {
    'Timestamp': pd.date_range(end=datetime.now(), periods=8, freq='H'),
    'Type': ['Delay Pattern', 'Staff Utilization', 'Queue Spike', 'Baggage System', 
             'Passenger Flow', 'Gate Assignment', 'Revenue Drop', 'Weather Impact'],
    'Severity': ['High', 'Critical', 'Medium', 'High', 'Low', 'Medium', 'Critical', 'High'],
    'Score': [0.92, 0.95, 0.67, 0.88, 0.45, 0.72, 0.91, 0.84],
}

df_anomalies = pd.DataFrame(anomalies_data)
df_anomalies = df_anomalies[df_anomalies['Severity'].isin(severity_filter)]
st.dataframe(df_anomalies, use_container_width=True, hide_index=True)
