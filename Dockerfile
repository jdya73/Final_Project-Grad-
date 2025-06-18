
FROM python:3.10-slim
WORKDIR /app
COPY smart_city_iot_dataset.csv .
COPY stream_metrics.py .
RUN pip install flask pandas prometheus_client
CMD ["python", "stream_metrics.py"]
