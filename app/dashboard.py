import streamlit as st
import pandas as pd


def render_dashboard(metrics, state, risk, confidence, recommendation):

    st.title("AI Pharmacy Delivery Dispatch Control")

    st.subheader("Operational KPIs")

    col1, col2, col3 = st.columns(3)

    col1.metric("Deliveries Today", metrics["deliveries_today"])
    col2.metric("On-time Rate", round(metrics["on_time_rate"], 3))
    col3.metric("Avg Delay (min)", metrics["avg_delay_minutes"])

    st.subheader("System State Vector")

    st.json(state)

    st.subheader("System Risk")

    st.metric("Risk Score", risk["risk_score"])
    st.write("Risk Level:", risk["risk_level"])

    st.subheader("Confidence Mode")

    st.metric("Confidence Score", confidence["confidence_score"])
    st.write("Mode:", confidence["confidence_mode"])

    st.subheader("Dispatch Recommendation")

    st.write(recommendation["decision_mode"])
    st.write(recommendation["recommendation"])

    st.subheader("Zone Delivery Load")

    st.dataframe(metrics["zone_load"])