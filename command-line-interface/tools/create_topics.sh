#!/bin/bash
for i in <topic-name>
do
    echo $i
    docker exec -it <broker> kafka-topics --bootstrap-server <host:port> --create --topic $i --partitions 10 --replication-factor 5
done

