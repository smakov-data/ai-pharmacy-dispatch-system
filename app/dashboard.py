import streamlit as st
import pandas as pd
from pathlib import Path
from themes import THEMES

def format_ai_insight(text):

    text = text.replace("CEI", "<span class='metric-name'>CEI</span>")
    text = text.replace("CLI", "<span class='metric-name'>CLI</span>")
    text = text.replace("NODI", "<span class='metric-name'>NODI</span>")
    text = text.replace("WBI", "<span class='metric-name'>WBI</span>")

    text = text.replace("CRITICAL", "<span class='metric-critical'>CRITICAL</span>")
    text = text.replace("LOW", "<span class='metric-low'>LOW</span>")
    text = text.replace("HIGH", "<span class='metric-high'>HIGH</span>")

    return text

def render_dashboard(metrics, state, risk, confidence, recommendation, ai_summary):
    #Theme
    theme_name = st.selectbox("Control Skin", list(THEMES.keys()))
    theme = THEMES[theme_name]

    css_path = Path(__file__).parent.parent / "ui" / "styles.css"

    #css
    with open(css_path) as f:
        css = f.read()

    css = (
        css.replace("__BG__", theme["bg"])
        .replace("__ACCENT__", theme["accent"])
        .replace("__TEXT__", theme["text"])
        .replace("__MUTED__", theme["muted"])
        .replace("__PANEL__", theme["panel"])
        .replace("__BORDER__", theme["border"])
    )

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    #Title
    st.title("AI Pharmacy Delivery Dispatch Control")
    st.caption(f"Active skin: {theme_name}")

    st.subheader("Operational KPIs")

    col1, col2, col3 = st.columns(3)
    col1.metric("Deliveries Today", metrics["deliveries_today"])
    col2.metric("On-time Rate", round(metrics["on_time_rate"], 3))
    col3.metric("Avg Delay (min)", metrics["avg_delay_minutes"])

    #State Vector
    st.subheader("System State Vector")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("CEI", round(state["CEI"], 3))
    col2.metric("CLI", round(state["CLI"], 3))
    col3.metric("NODI", round(state["NODI"], 3))
    col4.metric("WBI", round(state["WBI"], 3))

    # Risk and Confidence
    st.subheader("System Risk and Confidence")
    col1, col2 = st.columns(2)

    col1.metric("Risk Score", round(risk["risk_score"], 3))
    risk_level = risk["risk_level"]

    if risk_level == "CRITICAL":
        col1.markdown("<span style='color:#FF3B3B; font-weight:700;'>Risk Level: CRITICAL</span>", unsafe_allow_html=True)
    elif risk_level == "HIGH":
        col1.markdown("<span style='color:#FFD84D; font-weight:700;'>Risk Level: HIGH</span>", unsafe_allow_html=True)
    elif risk_level == "MEDIUM":
        col1.markdown("<span style='color:#FFD84D; font-weight:700;'>Risk Level: MEDIUM</span>", unsafe_allow_html=True)
    else:
        col1.markdown(f"<span style='color:{theme['accent']}; font-weight:700;'>Risk Level: {risk_level}</span>", unsafe_allow_html=True)

    col2.metric("Confidence Score", round(confidence["confidence_score"], 3))
    confidence_mode = confidence["confidence_mode"]

    if confidence_mode == "LOW":
        col2.markdown("<span style='color:#FF3B3B; font-weight:700;'>Confidence Mode: LOW</span>", unsafe_allow_html=True)
    elif confidence_mode == "MEDIUM":
        col2.markdown("<span style='color:#FFD84D; font-weight:700;'>Confidence Mode: MEDIUM</span>", unsafe_allow_html=True)
    else:
        col2.markdown(f"<span style='color:{theme['accent']}; font-weight:700;'>Confidence Mode: HIGH</span>", unsafe_allow_html=True)

    # Decision Mode
    st.subheader("Decision Mode")
    mode = recommendation["decision_mode"]

    if mode == "FALLBACK_RULE":
        st.markdown("<span style='color:#FF3B3B; font-weight:700;'>FALLBACK_RULE</span>", unsafe_allow_html=True)
    elif mode == "AI_ADVISORY":
        st.markdown("<span style='color:#FFD84D; font-weight:700;'>AI_ADVISORY</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='color:{theme['accent']}; font-weight:700;'>AI_RECOMMENDATION</span>", unsafe_allow_html=True)

    #Recommendation
    st.subheader("Dispatch Recommendation")

    st.markdown(
        f"""
        <div class="recommendation-box">
        {recommendation["recommendation"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    #AI insight
    st.subheader("AI Operational Insight")
    formatted_insight = format_ai_insight(ai_summary)

    st.markdown(
        f"""
        <div class="ai-box">
        {formatted_insight}
        </div>
        """,
        unsafe_allow_html=True
    )

    #Load
    st.subheader("Zone Delivery Load")
    st.dataframe(metrics["zone_load"])
