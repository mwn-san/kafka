# Getting Started
```
docker-compose up -d ZK731
```
```
sh add_sasl-scram_user_kafka_zookeeper.sh
```
```
docker-compose up -d BK731
```
```
docker-compose up -d SR731 C3731
```

### Ensure the service port for each module is active using the command below:

| Service          | Ports                      |
|:-----------------|:---------------------------|
| zookeeper        | 2181, 2182, 2888, 3888     |
| broker           | 9092, 9093, 9094           |
| schema registry  | 8081, 8082                 |
| control center   | 9021, 9022                 |

```
netstat -plnt | grep <port>
```

### How to check SASL/SCRAM users Kafka on Zookeeper shell.
```
docker exec -ti <ontainer-name> /bin/bash
```
```
zookeeper-shell localhost:2181
```
```
ls /config/users
```
### How to delete SASL/SCRAM users.
```
deleteall /config/users/name_of_user
```
### How to add ACLs operation (resources: topic - group).
```
kafka-acls --bootstrap-server <host>:<port> \
           --command-config /etc/kafka/helper/adminclient-configs.conf \
           --add \
           --allow-principal User:digital \
           --allow-host 10.10.10.6 \
           --operation Create \
           --operation Describe \
		       --operation Write \
           --topic finance-syariah
```
```
kafka-acls --bootstrap-server <host>:<port> \
           --command-config /etc/kafka/helper/adminclient-configs.conf \
           --add \
           --allow-principal User:streaming \
           --operation Read \
           --operation Describe \
           --topic finance-syariah \
           --group finance-syariah-group
```

### How to delete ACLs operation.
```
kafka-acls --bootstrap-server <host>:<port> \
           --command-config /etc/kafka/helper/adminclient-configs.conf \
           --remove \
           --allow-principal User:digital \
           --operation CREATE \
           --operation DESCRIBE \
           --operation READ \
           --operation WRITE \
           --topic finance-syariah \
           --force
```
```
kafka-acls --bootstrap-server <host>:<port> \
           --command-config /etc/kafka/helper/adminclient-configs.conf \
           --remove 
           --allow-principal User:digital \
           --operation CREATE \
           --operation DESCRIBE \
           --operation READ \
           --operation WRITE \
           --topic finance-syariah 
           --allow-host 10.10.10.6
```
```
kafka-acls --bootstrap-server <host>:<port> \
           --command-config /etc/kafka/helper/adminclient-configs.conf \
           --remove 
           --allow-principal User:digital \
           --group finance-syariah-group \
           --operation READ \
           --operation DESCRIBE
```
