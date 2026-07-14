"""
06_Reports.py
--------------
Automated report generation.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import io

st.set_page_config(page_title="Reports", page_icon="📄", layout="wide")

st.title("📄 Reports")
st.markdown("Generate and download operational reports")

col1, col2, col3 = st.columns(3)

with col1:
    report_type = st.selectbox("Report Type", ["Daily Summary", "Weekly Analysis", "Monthly Review", "Custom Period"])

with col2:
    if report_type == "Custom Period":
        start_date = st.date_input("Start Date", datetime.now() - pd.Timedelta(days=30))
with col3:
    if report_type == "Custom Period":
        end_date = st.date_input("End Date", datetime.now())

st.markdown("---")

st.subheader("Report Preview")

report_content = f"""
# AIRPORT OPERATIONS REPORT
**Period**: {report_type}  
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## EXECUTIVE SUMMARY
- Total Flights: 247
- On-Time Performance: 77.5%
- Average Delay: 33.9 minutes
- Daily Passengers: 30,841
- System Uptime: 99.98%

## KPI SUMMARY
| Metric | Value | Trend |
|--------|-------|-------|
| On-Time Performance | 77.5% | ↓ 2.5% |
| Avg Delay Duration | 33.9 min | ↑ 5.2 min |
| Avg Queue Wait Time | 7.9 min | ↓ 0.5 min |
| Baggage Mishandling Rate | 0.698% | ↑ 0.098% |
| Staff Utilization | 89% | ↑ 3% |

## KEY INSIGHTS
1. Weather is the strongest predictor of delays (correlation = 0.91)
2. On-time performance below 80% industry benchmark
3. Staff utilization above optimal on 50% of days
4. Baggage mishandling rate exceeds 0.5% target
"""

st.markdown(report_content)

st.markdown("---")

st.subheader("Download Report")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📥 Download as PDF"):
        st.success("PDF generated successfully!")

with col2:
    if st.button("📊 Download as Excel"):
        st.success("Excel file generated!")

with col3:
    if st.button("📋 Download as CSV"):
        st.success("CSV file generated!")

st.markdown("---")

st.subheader("Email Report")

with st.form("email_form"):
    recipient_email = st.text_input("Recipient Email")
    submitted = st.form_submit_button("Send Email")
    if submitted:
        st.success(f"✅ Report sent to {recipient_email}")
