#!/bin/bash

KAFKA_CONNECT_URL="http://<host>:<port>"

connectors=$(curl -s "$KAFKA_CONNECT_URL/connectors")

for connector in $(echo $connectors | jq -r '.[]'); do
    echo "Pausing connector: $connector"
    curl -X PUT "$KAFKA_CONNECT_URL/connectors/$connector/resume" -o /dev/null
done

echo "CONNECTORS HAVE BEEN RESUMED."

