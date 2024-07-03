import csv
import os

# Input file name
filename = './../data/iot_telemetry_data.csv'
temp_filename = 'temp.csv'

# Device ID to target
target_device_id = '00:0f:00:70:91:0a'

# Initialize counters for the target device
device_temp_count = 0

# Read the data from the CSV file line by line and write to a temporary file
with open(filename, mode='r', newline='') as infile, open(temp_filename, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    
    for row in reader:
        if row['device'] == target_device_id:
            device_temp_count += 1
            if 21 <= device_temp_count <= 30:
                row['temp'] = '55'
        writer.writerow(row)

# Replace the original file with the modified file
os.replace(temp_filename, filename)

print(f'Modified data has been written back to {filename}')
