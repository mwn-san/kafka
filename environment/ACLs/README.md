### HOW TO CHECK SASL/SCRAM USERS KAFKA ON ZOOKEEPER SHELL

docker exec -ti <ontainer-name> /bin/bash

zookeeper-shell localhost:2181

ls /config/users

### HOW TO DELETE SASL/SCRAM USERS 
deleteall /config/users/name_of_user

### HOW TO ADD ACLS OPERATION (RESOURCES : TOPIC - GROUP)
kafka-acls --bootstrap-server <host>:<port> \
           --command-config /etc/kafka/helper/adminclient-configs.conf \
           --add \
           --allow-principal User:digital \
           --allow-host 10.10.10.6 \
           --operation Create \
           --operation Describe \
		       --operation Write \
           --topic finance-syariah

kafka-acls --bootstrap-server <host>:<port> \
           --command-config /etc/kafka/helper/adminclient-configs.conf \
           --add \
           --allow-principal User:streaming \
           --operation Read \
           --operation Describe \
           --topic finance-syariah \
		       --group finance-syariah-group

### HOW TO DELETE ACLS OPERATION

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

kafka-acls --bootstrap-server <host>:<port> \
           --command-config /etc/kafka/helper/adminclient-configs.conf \
           --remove 
           --allow-principal User:digital \
           --group finance-syariah-group \
           --operation READ \
           --operation DESCRIBE
