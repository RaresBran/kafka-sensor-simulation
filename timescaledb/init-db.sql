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

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(255) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL
);

-- Create tokens table
CREATE TABLE IF NOT EXISTS tokens (
    id VARCHAR(255) PRIMARY KEY,
    expired BOOLEAN NOT NULL,
    revoked BOOLEAN NOT NULL,
    token VARCHAR(1024) NOT NULL,
    token_type VARCHAR(255) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
