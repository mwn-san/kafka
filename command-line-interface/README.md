# Getting Started
Go to broker shell ($):

kafka-console-producer
```bash
kafka-console-producer --topic <topic_name> --bootstrap-server <host:port>

# enter this following example messages:
message-0
message-1
message-2
message-3
message-4
```
kafka-console-consumer
```bash
kafka-console-consumer --topic <topic_name> --bootstrap-server <host:port> --from-beginning
```
