from prometheus_client import start_http_server, Gauge
import pandas as pd
import time
import random

df = pd.read_csv("smart_city_iot_dataset.csv")

cpu_usage = Gauge('cpu_usage', 'CPU Usage by IoT service', ['device_id', 'service_type'])
energy = Gauge('energy_consumed_watts', 'Energy usage', ['device_id'])
latency = Gauge('latency_ms', 'Service latency', ['service_type'])

# Start Prometheus metrics server
start_http_server(8000)
print("✅ Prometheus metrics available at :8000")

while True:
    sample = df.sample(1).iloc[0]
    cpu_usage.labels(sample.device_id, sample.service_type).set(sample.cpu_usage)
    energy.labels(sample.device_id).set(sample.energy_consumed_watts)
    latency.labels(sample.service_type).set(sample.latency_ms)
    print(f"Pushed metrics for {sample.device_id} ({sample.service_type})")
    time.sleep(5)

