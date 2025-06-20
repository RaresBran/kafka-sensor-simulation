# IoT Sensor Simulation with Kafka

This repository provides a small environment for generating and streaming IoT telemetry data. A set of Python scripts read sample measurements from `data/iot_telemetry_data.csv` and publish them to Kafka topics. The included Docker Compose stack exposes Kafka together with supporting services such as Grafana, TimescaleDB and Redis so you can experiment with streaming pipelines locally.

## Components

- **sensor-simulator.py** – streams the sample dataset to Kafka on a regular interval.
- **bad-sensor-simulator.py** – injects incorrect timestamps to mimic faulty sensors.
- **null-sensor-simulator.py** – sends occasional `null` temperature values.
- **docker-compose.yml** – starts Kafka, Zookeeper, Storm, TimescaleDB, Grafana, Redis and helper services.

## Prerequisites

- Docker and Docker Compose
- Python 3 with the `confluent-kafka` package if you want to run the simulators outside of Docker

Install the Python dependency:

```bash
pip install confluent-kafka
```

## Running the stack

1. Clone the repository and change into the directory:

   ```bash
git clone https://github.com/your-username/kafka-sensor-simulation.git
cd kafka-sensor-simulation
   ```

2. Start all services with Docker Compose:

   ```bash
docker-compose up --build
   ```

   Kafka will be available on `localhost:9092` once all containers are running.

## Simulating sensors

Use one of the simulator scripts from a separate shell to begin publishing events:

```bash
python sensor-simulator.py             # normal data
python bad-sensor-simulator.py         # timestamps anomalies
python null-sensor-simulator.py        # occasional null values
```

Each script will create the required Kafka topics if they do not already exist.

## Grafana dashboards

Grafana listens on [http://localhost:3000](http://localhost:3000) and is preconfigured with a connection to TimescaleDB. The default credentials are `admin` / `admin`.

## Project structure

```
.
├── Dockerfile                 # Image for Storm containers
├── docker-compose.yml         # Service definitions
├── sensor-simulator.py        # Baseline data stream
├── bad-sensor-simulator.py    # Faulty values example
├── null-sensor-simulator.py   # Null value example
├── data/                      # Sample CSV input
├── grafana/                   # Dashboard provisioning
├── redis/                     # Redis configuration
└── timescaledb/               # Database initialization
```

This setup is intended for demos or experimentation with stream processing frameworks. Feel free to modify the data or the simulators to match your own scenarios.

