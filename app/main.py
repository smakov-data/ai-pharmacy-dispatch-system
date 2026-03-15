import streamlit as st

from data_loader import load_data
from metrics import compute_base_metrics
from control_indices import compute_state_vector
from risk_engine import compute_risk
from confidence_engine import compute_confidence_state
from recommendation_engine import build_recommendation
from ai_summary import generate_ai_summary
from dashboard import render_dashboard

def main():

    deliveries, couriers, pharmacies = load_data()

    metrics = compute_base_metrics(deliveries, couriers)

    state = compute_state_vector(deliveries, couriers, pharmacies)

    risk = compute_risk(state)

    confidence = compute_confidence_state(state)

    recommendation = build_recommendation(state, risk, confidence)

    ai_summary = generate_ai_summary(state, risk, confidence, recommendation)

    render_dashboard(metrics, state, risk, confidence, recommendation, ai_summary)


if __name__ == "__main__":
    main()