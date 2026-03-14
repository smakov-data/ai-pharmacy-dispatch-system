import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)

# ----------------------------
# Configuration
# ----------------------------

NUM_PHARMACIES = 12
NUM_COURIERS = 50
NUM_DELIVERIES = 3000

ZONES = ["33101", "33109", "33139", "33132", "33137"]

TRAFFIC_LEVELS = ["low", "medium", "high"]
PRIORITY_LEVELS = ["normal", "urgent"]

VEHICLE_TYPES = ["bike", "car", "scooter"]
EXPERIENCE_LEVELS = ["junior", "mid", "senior"]

# ----------------------------
# Generate Pharmacies
# ----------------------------

pharmacies = []

for i in range(NUM_PHARMACIES):
    pharmacy_id = f"P{i:03d}"
    zone = random.choice(ZONES)
    
    pharmacies.append({
        "pharmacy_id": pharmacy_id,
        "pharmacy_name": f"Pharmacy_{pharmacy_id}",
        "zone": zone,
        "daily_capacity": random.randint(120, 250)
    })

pharmacies_df = pd.DataFrame(pharmacies)

# ----------------------------
# Generate Couriers
# ----------------------------

couriers = []

for i in range(NUM_COURIERS):
    courier_id = f"C{i:03d}"
    region = random.choice(ZONES)
    
    couriers.append({
        "courier_id": courier_id,
        "vehicle_type": random.choice(VEHICLE_TYPES),
        "experience_level": random.choice(EXPERIENCE_LEVELS),
        "region": region,
        "max_capacity": random.randint(3, 7)
    })

couriers_df = pd.DataFrame(couriers)

# ----------------------------
# Generate Deliveries
# ----------------------------

deliveries = []

now = datetime.now()

for i in range(NUM_DELIVERIES):

    delivery_id = f"D{i:05d}"

    pharmacy = pharmacies_df.sample(1).iloc[0]
    courier = couriers_df.sample(1).iloc[0]

    zone = pharmacy["zone"]

    order_time = now - timedelta(minutes=random.randint(0, 360))

    promised_time = order_time + timedelta(minutes=random.randint(25, 45))

    delay = np.random.normal(0, 10)
    delivered_time = promised_time + timedelta(minutes=max(delay, -5))

    distance = round(np.random.uniform(0.5, 6), 2)

    deliveries.append({
        "delivery_id": delivery_id,
        "pharmacy_id": pharmacy["pharmacy_id"],
        "courier_id": courier["courier_id"],
        "zone": zone,
        "order_created_at": order_time,
        "promised_time": promised_time,
        "delivered_time": delivered_time,
        "distance_miles": distance,
        "traffic_level": random.choice(TRAFFIC_LEVELS),
        "priority": random.choice(PRIORITY_LEVELS),
        "weather_flag": random.choice([0, 1]),
        "status": "delivered"
    })

deliveries_df = pd.DataFrame(deliveries)

# ----------------------------
# Save Data
# ----------------------------

pharmacies_df.to_csv("data/pharmacies.csv", index=False)
couriers_df.to_csv("data/couriers.csv", index=False)
deliveries_df.to_csv("data/deliveries.csv", index=False)

print("Synthetic data generated successfully.")