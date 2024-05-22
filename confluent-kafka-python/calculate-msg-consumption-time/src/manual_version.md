# FUNCTION 
```bash
def function_calculate_time_to_consume_messages(total_messages, messages_per_interval, interval_duration):

    # Calculates throughput per second
    throughput_per_second = messages_per_interval / interval_duration

    # Calculates total time in seconds
    total_seconds = total_messages / throughput_per_second

    # Convert total seconds to hours and minutes
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) / 60)

    return hours, minutes
```

# MAIN
```
```bash	
import json
from function import calculate_time_to_consume_messages

# Open and read configuration files
with open('config.json', 'r') as file:
    config = json.load(file)

# Call the function with data from the configuration file
hours, minutes = calculate_time_to_consume_messages(config['total_messages'], config['messages_per_interval'], config['interval_duration'])
print(f"Estimated time to consume all messages: {hours} hours and {minutes} minutes")
```
# CONFIGURATION ADJUSTMENT
```bash
# The values for "total messages" and "messages per interval" are adjusted to suit your needs
{
    "total_messages": 7867803,
    "messages_per_interval": 4913,
    "interval_duration": 5
}
