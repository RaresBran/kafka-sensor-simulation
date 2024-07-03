import csv
import time
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Producer, KafkaException
import json
import threading

KAFKA_BROKER = 'localhost:9092'
CSV_FILE = 'data/iot_telemetry_data.csv'
INTERVAL = 1  # seconds

TOPIC_MAP = {
    "b8:27:eb:bf:9d:51": "sensor1-data",
    "00:0f:00:70:91:0a": "sensor2-data",
    "1c:bf:ce:15:ec:4d": "sensor3-data"
}

def check_kafka_connection(broker):
    admin_client = AdminClient({'bootstrap.servers': broker})
    try:
        cluster_metadata = admin_client.list_topics(timeout=10)
        print(f"Connected to Kafka broker at {broker}")
        print(f"Available topics: {cluster_metadata.topics}")
        return True
    except KafkaException as e:
        print(f"Failed to connect to Kafka broker at {broker}: {e}")
        return False

def create_topics(admin_client, topics):
    new_topics = [NewTopic(topic, num_partitions=1, replication_factor=1) for topic in topics]
    fs = admin_client.create_topics(new_topics)
    
    # Wait for each operation to finish.
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print(f"Topic {topic} created")
        except Exception as e:
            print(f"Failed to create topic {topic}: {e}")

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

def produce_sensor_data(producer, topic, data):
    producer.produce(topic, value=json.dumps(data))
    producer.flush()

def emit_data(producer, device_id, topic, sensor_data):
    count = 0
    for data in sensor_data:
        if data['device'] == device_id:
            # Update the timestamp field with the current time in milliseconds
            data['ts'] = int(time.time() * 1000)
            
            # Introduce a null value in the temp column every 10 rows
            if device_id == "00:0f:00:70:91:0a" and count % 10 == 9:
                data['temp'] = None
            
            produce_sensor_data(producer, topic, data)
            # print(f"Produced to {topic}: {data}")
            time.sleep(INTERVAL)
            count += 1

def main():
    if not check_kafka_connection(KAFKA_BROKER):
        print("Exiting due to failed Kafka connection.")
        return

    admin_client = AdminClient({'bootstrap.servers': KAFKA_BROKER})
    create_topics(admin_client, TOPIC_MAP.values())

    producer = Producer({'bootstrap.servers': KAFKA_BROKER})
    
    sensor_data = list(read_csv(CSV_FILE))
    
    threads = []
    for device_id, topic in TOPIC_MAP.items():
        thread = threading.Thread(target=emit_data, args=(producer, device_id, topic, sensor_data))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
