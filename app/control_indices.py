import pandas as pd
from datetime import timedelta


def compute_cei(deliveries: pd.DataFrame, couriers: pd.DataFrame):
    now = deliveries["order_created_at"].max()
    active_window_start = now - timedelta(minutes=45)

    active_deliveries = deliveries[
        deliveries["order_created_at"] >= active_window_start
    ]

    courier_load = (
        active_deliveries.groupby("courier_id")
        .size()
        .reset_index(name="active_deliveries")
    )

    courier_load = courier_load.merge(couriers, on="courier_id", how="left")
    courier_load["cei"] = courier_load["active_deliveries"] / courier_load["max_capacity"]

    if courier_load.empty:
        return 0.0

    return round(float(courier_load["cei"].mean()), 3)


def compute_cli(deliveries: pd.DataFrame):
    delayed = deliveries["delivered_time"] > deliveries["promised_time"]
    cli = delayed.sum() / len(deliveries)
    return round(float(cli), 3)


def compute_nodi(deliveries: pd.DataFrame):
    now = deliveries["order_created_at"].max()
    last_hour = now - timedelta(hours=1)

    new_orders_last_hour = deliveries[
        deliveries["order_created_at"] >= last_hour
    ].shape[0]

    total_hours = (
        deliveries["order_created_at"].max() - deliveries["order_created_at"].min()
    ).total_seconds() / 3600

    avg_orders_per_hour = len(deliveries) / total_hours

    if avg_orders_per_hour == 0:
        return 0.0

    nodi = new_orders_last_hour / avg_orders_per_hour
    return round(float(nodi), 3)


def compute_wbi(deliveries: pd.DataFrame, pharmacies: pd.DataFrame):
    now = deliveries["order_created_at"].max()
    last_30 = now - timedelta(minutes=30)

    outbound_ready_orders = deliveries[
        deliveries["order_created_at"] >= last_30
    ].shape[0]

    dispatch_processing_capacity = pharmacies["daily_capacity"].sum() / 24

    if dispatch_processing_capacity == 0:
        return 0.0

    wbi = outbound_ready_orders / dispatch_processing_capacity
    return round(float(wbi), 3)


def compute_state_vector(deliveries, couriers, pharmacies):
    return {
        "CEI": compute_cei(deliveries, couriers),
        "CLI": compute_cli(deliveries),
        "NODI": compute_nodi(deliveries),
        "WBI": compute_wbi(deliveries, pharmacies),
    }