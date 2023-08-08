import pandas as pd
import matplotlib.pyplot as plt

log_lines = pd.read_csv('log_lines.csv', parse_dates=['timestamp'])
log_lines['color'] = log_lines['path'].apply(lambda p: 'red' if "/getAppData" in p else "black")

start_timestamp = "2023-08-08 12:00:05.356532+00:00"
end_timestamp = "2023-08-08 12:30:05.356532+00:00"

log_lines = log_lines[(log_lines["timestamp"] > start_timestamp) & (log_lines["timestamp"] < end_timestamp)]

plt.figure(figsize=(10, 6))
plt.scatter(log_lines['timestamp'], log_lines['service'], marker='o', linestyle='-', c=log_lines["color"])
plt.xlabel('Timestamp')
plt.ylabel('Response time')
plt.title('Response time of different requests (red marks items of interest)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
