import pandas as pd


def compute_base_metrics(deliveries: pd.DataFrame, couriers: pd.DataFrame) -> dict:
    deliveries = deliveries.copy()

    deliveries["delay_minutes"] = (
        deliveries["delivered_time"] - deliveries["promised_time"]
    ).dt.total_seconds() / 60

    deliveries_today = len(deliveries)

    on_time_rate = (deliveries["delay_minutes"] <= 0).mean()

    avg_delay = deliveries.loc[deliveries["delay_minutes"] > 0, "delay_minutes"].mean()
    avg_delay = 0 if pd.isna(avg_delay) else round(avg_delay, 2)

    courier_load = deliveries.groupby("courier_id").size().reset_index(name="delivery_count")
    courier_util = courier_load.merge(couriers, on="courier_id", how="left")
    courier_util["utilization"] = courier_util["delivery_count"] / courier_util["max_capacity"]

    avg_courier_utilization = round(courier_util["utilization"].mean(), 2)

    overloaded_couriers = int((courier_util["utilization"] > 1).sum())

    zone_load = deliveries.groupby("zone").size().reset_index(name="delivery_count")

    return {
        "deliveries_today": deliveries_today,
        "on_time_rate": round(on_time_rate, 4),
        "avg_delay_minutes": avg_delay,
        "avg_courier_utilization": avg_courier_utilization,
        "overloaded_couriers": overloaded_couriers,
        "zone_load": zone_load,
        "courier_utilization_table": courier_util,
    }