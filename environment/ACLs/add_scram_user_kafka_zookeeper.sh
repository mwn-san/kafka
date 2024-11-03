#!/bin/bash

for i in admin client digital streaming developer

do
        echo $i

docker exec -it <container_name> kafka-configs --zookeeper localhost:2181 --alter --add-config 'SCRAM-SHA-256=[password=confluent],SCRAM-SHA-512=[password=confluent]' --entity-type users --entity-name $i

docker exec -it <container_name> kafka-configs --zookeeper localhost:2181 --describe --entity-type users --entity-name $i

done
