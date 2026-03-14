import streamlit as st

from data_loader import load_data
from metrics import compute_base_metrics
from control_indices import compute_state_vector
from risk_engine import compute_risk
from confidence_engine import compute_confidence_state
from recommendation_engine import build_recommendation
from dashboard import render_dashboard

def main():

    deliveries, couriers, pharmacies = load_data()

    metrics = compute_base_metrics(deliveries, couriers)

    state = compute_state_vector(deliveries, couriers, pharmacies)

    risk = compute_risk(state)

    confidence = compute_confidence_state(state)

    recommendation = build_recommendation(state, risk, confidence)

    render_dashboard(metrics, state, risk, confidence, recommendation)


if __name__ == "__main__":
    main()