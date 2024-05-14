import json
from consumer_lag_time import calculate_time_to_consume_messages

# Membuka dan membaca file konfigurasi
with open('config.json', 'r') as file:
    config = json.load(file)

# Memanggil fungsi dengan data dari file konfigurasi
hours, minutes = calculate_time_to_consume_messages(config['total_messages'], config['messages_per_interval'], config['interval_duration'])
print(f"Estimated time to consume all messages: {hours} hours and {minutes} minutes")
