# AI Dispatch Decision System

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

## System Architecture

The system transforms simulated delivery operations into operational metrics, derives a system state vector, evaluates risk, and produces dispatch decisions displayed in the dashboard.

<img src="docs/system_architecture.png" width="700">

## Tech Stack

Python  
Pandas  
NumPy  
Streamlit

## Run

pip install -r requirements.txt  
streamlit run app/dashboard.py

## Example Output

Dashboard showing:

- Operational KPIs
- System Risk Score
- Dispatch Recommendation
- Zone Delivery Load


Example system dashboard:
<img src="docs/dashboard.png" width="800">
