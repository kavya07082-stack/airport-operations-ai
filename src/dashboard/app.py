"""
app.py
------
Streamlit main app entry point - Airport Operations Dashboard
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

from src.utils.config import config
from src.utils.logger import get_logger

logger = get_logger(__name__)

# Page config
st.set_page_config(
    page_title="Airport Operations Dashboard",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
    }
    .alert-high {
        background-color: #ffe5e5;
        border-left: 4px solid #ff0000;
    }
    .alert-medium {
        background-color: #fff3e5;
        border-left: 4px solid #ff9800;
    }
    .alert-low {
        background-color: #e5f5e5;
        border-left: 4px solid #4caf50;
    }
    </style>
""", unsafe_allow_html=True)


def init_session_state():
    """Initialize session state variables."""
    if "selected_date" not in st.session_state:
        st.session_state.selected_date = datetime.now().date()
    if "forecast_horizon" not in st.session_state:
        st.session_state.forecast_horizon = 30
    if "anomaly_threshold" not in st.session_state:
        st.session_state.anomaly_threshold = config.ANOMALY_THRESHOLD


def display_header():
    """Display dashboard header."""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.title("✈️ Airport Operations Dashboard")
        st.markdown("*Real-time monitoring & predictive analytics*")
    
    with col3:
        st.metric("Last Updated", datetime.now().strftime("%H:%M:%S"))


def display_kpi_cards():
    """Display key performance indicators."""
    st.subheader("📊 Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("On-Time Performance", "77.5%", "-2.5%", delta_color="inverse")
    
    with col2:
        st.metric("Avg Delay", "33.9 min", "+5.2 min", delta_color="inverse")
    
    with col3:
        st.metric("Daily Passengers", "30,841", "+1,245")
    
    with col4:
        st.metric("Queue Time", "7.9 min", "-0.5 min")


def display_alerts():
    """Display active alerts."""
    st.subheader("⚠️ Active Alerts")
    
    alerts = [
        {"type": "High Staff Utilization", "severity": "high", "message": "Boarding area at 95% capacity"},
        {"type": "Delay Alert", "severity": "medium", "message": "Flight BA847 delayed by 25 minutes"},
        {"type": "Queue Time", "severity": "low", "message": "Security queue time elevated"},
    ]
    
    for alert in alerts:
        severity_class = f"alert-{alert['severity']}"
        st.markdown(f"""
        <div class="{severity_class}" style="padding: 15px; border-radius: 5px; margin-bottom: 10px;">
            <strong>{alert['type']}</strong> ({alert['severity'].upper()})<br>
            {alert['message']}
        </div>
        """, unsafe_allow_html=True)


def main():
    """Main app function."""
    init_session_state()
    
    display_header()
    st.markdown("---")
    display_kpi_cards()
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 📋 Navigation")
        st.info("Use the page selector above to navigate.")
        
        st.markdown("### ⚙️ Settings")
        st.session_state.forecast_horizon = st.slider(
            "Forecast Horizon (days)", 1, 90,
            st.session_state.forecast_horizon
        )
        
        st.session_state.anomaly_threshold = st.slider(
            "Anomaly Threshold", 0.0, 1.0,
            st.session_state.anomaly_threshold, 0.01
        )
    
    display_alerts()
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Airport Operations AI © 2024</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
