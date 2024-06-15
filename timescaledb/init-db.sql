-- Create sensor_data table if it does not exist
CREATE TABLE IF NOT EXISTS sensor_data (
    time TIMESTAMPTZ NOT NULL, 
    device VARCHAR(50) NOT NULL, 
    temperature DOUBLE PRECISION NOT NULL, 
    humidity DOUBLE PRECISION NOT NULL, 
    co DOUBLE PRECISION NOT NULL, 
    light INTEGER NOT NULL, 
    lpg DOUBLE PRECISION NOT NULL, 
    motion INTEGER NOT NULL, 
    smoke DOUBLE PRECISION NOT NULL, 
    rejected BOOLEAN NOT NULL, 
    suspicious BOOLEAN NOT NULL
);

-- Convert sensor_data into a hypertable
SELECT create_hypertable('sensor_data', 'time', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS event_alerts (
    time TIMESTAMPTZ NOT NULL,
    device VARCHAR(255) NOT NULL,
    event_type VARCHAR(255) NOT NULL,
    sensor_type VARCHAR(255) NOT NULL,
    value DOUBLE PRECISION NOT NULL,
    suspicious BOOLEAN NOT NULL
);

-- Create a hypertable if TimescaleDB extension is enabled
SELECT create_hypertable('event_alerts', 'time', if_not_exists => TRUE);
