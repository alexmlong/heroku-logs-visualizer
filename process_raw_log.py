import csv
from datetime import datetime
import re
import csv

with open("log_lines.txt", "r") as file:
    log_lines_text = file.read()

def extract_info(line):
    timestamp = line[:29]
    path_match = re.search(r'path="([^"]+)"', line)
    path = path_match.group(1) if path_match else None
    service_match = re.search(r'service=(\d+)ms', line)
    service = service_match.group(1) if service_match else None
    return timestamp, path, service

lines = log_lines_text.strip().split('\n')
lines = list(filter(lambda l: "heroku[router]" in l, lines))

data = [extract_info(line) for line in lines]

csv_filename = "log_lines.csv"
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['timestamp', 'path', 'service'])
    csv_writer.writerows(data)

print(f"CSV file '{csv_filename}' created successfully.")
