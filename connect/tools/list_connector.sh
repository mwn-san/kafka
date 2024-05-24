#!/bin/bash

KAFKA_CONNECT_URL="http://<host>:<port>"

CONNECTORS=$(curl -s "$KAFKA_CONNECT_URL/connectors")

echo "List of Connectors:"
echo $CONNECTORS | jq -r '.[]'

