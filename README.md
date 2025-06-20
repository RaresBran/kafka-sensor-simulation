# Kafka Sensor Simulation

This project simulates IoT sensor data using **Apache Kafka**, allowing you to generate realistic, null, and anomalous data for testing stream processing and monitoring setups. It includes optional visualization with **Grafana**, and storage using **TimescaleDB** and **Redis**.

## Features

- Simulate normal, faulty, and null sensor data
- Stream data via Kafka topics
- Preconfigured Docker setup (Kafka, Grafana, Redis, TimescaleDB)
- Custom data generation scripts
- Real-time monitoring via Grafana

## Technologies Used

- Python
- Apache Kafka
- Docker & Docker Compose
- Redis, TimescaleDB
- Grafana
- Pandas, Faker

## Project Structure

```
kafka-sensor-simulation/
└── kafka-sensor-simulation-main/
    ├── sensor-simulator.py              # Normal sensor data simulator
    ├── bad-sensor-simulator.py          # Injects faulty values
    ├── null-sensor-simulator.py         # Injects null values
    ├── data/iot_telemetry_data.csv      # Sample telemetry data
    ├── data_generators/                 # Additional data generator scripts
    ├── docker-compose.yml               # Docker orchestration
    ├── Dockerfile                       # Simulator container build
    ├── grafana/                         # Grafana provisioning
    ├── redis/                           # Redis config
    └── timescaledb/                     # DB init scripts
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/kafka-sensor-simulation.git
   cd kafka-sensor-simulation/kafka-sensor-simulation-main
   ```

2. **Start the environment**
   Make sure Docker is installed, then run:
   ```bash
   docker-compose up --build
   ```

3. **Run a sensor simulator**
   In a separate terminal:
   ```bash
   python sensor-simulator.py
   # or
   python bad-sensor-simulator.py
   # or
   python null-sensor-simulator.py
   ```

4. **Access Grafana**
   Open [http://localhost:3000](http://localhost:3000) in your browser.
   Default credentials: `admin` / `admin`
