"""
04_Optimization.py
------------------
Resource optimization recommendations.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import numpy as np

st.set_page_config(page_title="Optimization", page_icon="⚡", layout="wide")

st.title("⚡ Resource Optimization")
st.markdown("AI-powered recommendations for resource allocation")

col1, col2, col3 = st.columns(3)

with col1:
    optimization_target = st.selectbox("Optimize For", ["Cost Reduction", "Performance", "Efficiency", "Sustainability"])

with col2:
    time_horizon = st.selectbox("Time Horizon", ["Daily", "Weekly", "Monthly"])

with col3:
    constraints = st.multiselect("Constraints", ["Max Staff", "Min Service Level", "Budget", "Environmental"],
                                default=["Max Staff", "Budget"])

st.markdown("---")

st.subheader("Staff Allocation Analysis")

staff_data = {
    'Department': ['Baggage', 'Check-in', 'Security', 'Gates', 'Boarding', 'Ground Ops'],
    'Current': [45, 38, 52, 61, 28, 34],
    'Required': [42, 35, 50, 58, 32, 36],
    'Optimized': [43, 36, 50, 58, 30, 35],
    'Cost Saving': ['$300', '$200', '$200', '$300', '$400', '$100']
}

df_staff = pd.DataFrame(staff_data)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Staff Allocation Comparison")
    fig = go.Figure(data=[
        go.Bar(x=df_staff['Department'], y=df_staff['Current'], name='Current', marker_color='#1f77b4'),
        go.Bar(x=df_staff['Department'], y=df_staff['Optimized'], name='Optimized', marker_color='#2ca02c')
    ])
    fig.update_layout(height=400, barmode='group')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("### Potential Savings")
    savings = [int(s.replace('$', '').replace(',', '')) for s in df_staff['Cost Saving']]
    fig = go.Figure(data=[go.Bar(x=df_staff['Department'], y=savings,
                                marker_color=['#2ca02c' if s > 250 else '#ff7f0e' for s in savings])])
    fig.update_layout(height=400, title="Daily Cost Savings")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Optimization Results")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Cost Savings", "$1,500", "+5% vs last week")
with col2:
    st.metric("Staff Efficiency", "92.3%", "+3.2%")
with col3:
    st.metric("Gate Utilization", "82.5%", "-8.5%")
with col4:
    st.metric("Service Level", "99.2%", "+0.2%")
