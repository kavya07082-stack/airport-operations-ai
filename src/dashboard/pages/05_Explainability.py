"""
05_Explainability.py
--------------------
Model explainability analysis.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import numpy as np

st.set_page_config(page_title="Explainability", page_icon="🔍", layout="wide")

st.title("🔍 Model Explainability")
st.markdown("Understand model predictions with SHAP and LIME")

col1, col2, col3 = st.columns(3)

with col1:
    model_selection = st.selectbox("Select Model", ["XGBoost", "Random Forest", "LSTM", "Ensemble"])

with col2:
    explanation_method = st.selectbox("Explanation Method", ["SHAP", "LIME", "Feature Importance"])

with col3:
    instance_idx = st.number_input("Instance Index", min_value=0, max_value=100, value=0)

st.markdown("---")

st.subheader(f"Feature Importance - {model_selection}")

features = ['Weather Severity', 'Staff Utilization', 'Passenger Volume', 'Day of Week',
            'Queue Time', 'Wind Speed', 'Precipitation', 'Visibility', 'Temperature', 'Historical']
importances = np.array([0.35, 0.22, 0.18, 0.12, 0.08, 0.02, 0.01, 0.01, 0.00, 0.01])

fig = go.Figure(data=[go.Barh(x=importances, y=features, orientation='h',
                              marker_color=['#d62728' if x > 0.2 else '#ff7f0e' if x > 0.1 else '#2ca02c' for x in importances])])
fig.update_layout(title="Top Features Driving Predictions", xaxis_title="Importance", height=400)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

if explanation_method == "SHAP":
    st.subheader("SHAP Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### SHAP Summary Plot")
        shap_values = np.random.randn(len(features)) * 0.1
        fig = go.Figure(data=[go.Barh(x=np.abs(shap_values), y=features,
                                      marker_color=['#d62728' if x > 0.15 else '#2ca02c' for x in np.abs(shap_values)])])
        fig.update_layout(title="Mean |SHAP| Values", xaxis_title="Mean |SHAP value|", height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Prediction Breakdown")
        base_value = 30000
        contributions = {'Weather': 1500, 'Staff': 800, 'Passengers': 450, 'Day': 200, 'Queue': -100}
        fig = go.Figure()
        fig.add_trace(go.Waterfall(
            x=['Base Value'] + list(contributions.keys()) + ['Prediction'],
            y=[base_value] + list(contributions.values()) + [0],
            measure=['absolute'] + ['relative'] * len(contributions) + ['total'],
        ))
        fig.update_layout(title="Prediction Breakdown", height=400)
        st.plotly_chart(fig, use_container_width=True)

elif explanation_method == "LIME":
    st.subheader("LIME Local Explanations")
    st.markdown("Decision rules for this specific instance:")
    rules = [
        "Weather Severity > 0.7 → Increase prediction by +1200",
        "Staff Utilization > 1.0 → Increase prediction by +500",
        "Day of Week = Friday → Increase prediction by +800",
    ]
    for rule in rules:
        st.markdown(f"- {rule}")

else:
    st.subheader("Permutation Feature Importance")
    perm_importance = np.random.uniform(0, 0.4, len(features))
    perm_importance = perm_importance / perm_importance.sum()
    fig = go.Figure(data=[go.Bar(x=features, y=perm_importance, marker_color='#1f77b4')])
    fig.update_layout(title="Permutation Feature Importance", yaxis_title="Importance", height=400)
    st.plotly_chart(fig, use_container_width=True)
