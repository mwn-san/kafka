# Calculate Message Consumption Time
![alt text](https://github.com/mwn-san/confluent-kafka/blob/mwn/public/calculate_message_consumption_time.png?raw=true)
![alt text](https://github.com/mwn-san/confluent-kafka/blob/mwn/public/consumer_group_message_lag.png?raw=true)

This project is used to Calculate the time a Message has been Consumed on the Confluent Control Center (C3) Consumer Groups dashboard.

Created by Mohammad Wildan Nuryulda.
Hopefully it's useful
## Getting Started

1. Create a Python application directory:
   
   ```bash
   mkdir calculate-msg-consumption-time && calculate-msg-consumption-time
   mkdir src && mkdir templates && mkdir static
   
2. Install the necessary dependencies:
   ```bash
   sudo apt-get install python3-venv
   python3 -m venv venv
   source venv/bin/activate
   pip3 install flask
   pip list

3. Here's how to run the application:
   ```bash
   python3 app.py

4. Alternatively, to use nohup while keeping the virtual environment active:
   ```bash
   touch running-apps.sh && chmod +x running-apps.sh
   ```
   ```bash
   #!/bin/bash
   source /path/to/your/project/venv/bin/activate
   nohup sh -c '/path/to/your/project/python3 app.py > /path/to/your/project/output.log 2>&1' &
   ```
   ```bash
   ./running-apps.sh

   
