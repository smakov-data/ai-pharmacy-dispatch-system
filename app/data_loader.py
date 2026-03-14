import pandas as pd


def load_data():
    deliveries = pd.read_csv(
        "data/deliveries.csv",
        parse_dates=["order_created_at", "promised_time", "delivered_time"]
    )
    couriers = pd.read_csv("data/couriers.csv")
    pharmacies = pd.read_csv("data/pharmacies.csv")

    return deliveries, couriers, pharmacies