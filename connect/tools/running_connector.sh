#!/bin/bash

connect_api_url="${KAFKA_CONNECT_API_URL:-http://<host>:<port>}"

config_dir="${CONNECTOR_CONFIG_DIR:-/etc/kafka/connector-config}"

if [ ! -d "$config_dir" ]; then
    echo "Configuration directory not found: $config_dir"
    exit 1
fi

for config_file in "$config_dir"/*.json; do
    echo "Processing $config_file..."

    response=$(curl -s -X POST -H "Content-Type: application/json" --data "@$config_file" "$connect_api_url/connectors" -w "%{http_code}")

    http_code=$(echo "$response" | tail -n1)
    response_body=$(echo "$response" | head -n-1)

    if [ "$http_code" -eq 200 ] || [ "$http_code" -eq 201 ]; then
        echo "Connector created/updated successfully for config: $(basename "$config_file")"
        echo "$response_body"
    else
        echo "Failed to create/update connector for config: $(basename "$config_file"). HTTP status code: $http_code"
        echo "$response_body"
    fi

    echo "waiting for 30 seconds before processing the next file..."
    sleep 30
done

