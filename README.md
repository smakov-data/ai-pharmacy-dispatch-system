# AI Pharmacy Delivery Dispatch System

Applied AI system that simulates and monitors a pharmacy delivery network and produces operational dispatch recommendations based on system state and risk evaluation.

## Features

- Synthetic delivery network simulation
- Operational KPI monitoring
- System state vector (CEI, CLI, NODI, WBI)
- Risk scoring model
- Dispatch decision rules
- Interactive dashboard (Streamlit)

## Architecture

Synthetic Network → Metrics → State Vector → Risk Model → Dispatch Decision

## Tech Stack

Python  
Pandas  
NumPy  
Streamlit

## Run

pip install -r requirements.txt  
streamlit run dashboard.py

## Example Output

Dashboard showing:

- Operational KPIs
- System Risk Score
- Dispatch Recommendation
- Zone Delivery Load
