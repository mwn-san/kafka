#!/bin/bash

KAFKA_CONNECT_URL="http://PGD-JKT-CONNECT-01-DB.pegadaian.co.id:8083"

connectors=$(curl -s "$KAFKA_CONNECT_URL/connectors")

for connector in $(echo $connectors | jq -r '.[]'); do
    echo "Pausing connector: $connector"
    curl -X PUT "$KAFKA_CONNECT_URL/connectors/$connector/pause" -o /dev/null
done

echo "ALL CONNECTORS HAVE BEEN PAUSED."
