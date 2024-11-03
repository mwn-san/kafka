from confluent_kafka import DeserializingConsumer, OFFSET_BEGINNING
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import StringDeserializer

from datetime import datetime
import logging

def reset_offset(consumer, partitions):
    for p in partitions:
        p.offset = OFFSET_BEGINNING
    consumer.assign(partitions)

if __name__ == '__main__':
    # Setting up logging
    logging.basicConfig(filename='message.log', encoding='utf-8', level=logging.ERROR)

    # Configuration for Schema Registry with authentication
    sr_conf = {
        'url': 'http://<host>:<port>',
        'basic.auth.user.info': 'digital:confluent'  # Set Schema Registry authentication
    }
    schema_registry_client = SchemaRegistryClient(sr_conf)

    # Deserializers for key and value
    avro_key_deserializer = StringDeserializer('utf_8')
    avro_value_deserializer = AvroDeserializer(schema_registry_client)

    # Consumer configuration with ACL and client ID
    consumer_conf = {
        'bootstrap.servers': '<host>:<port>',
        'security.protocol': 'SASL_SSL',
        'sasl.mechanism': 'SCRAM-SHA-512',
        'sasl.username': 'digital',
        'sasl.password': 'confluent',
        'ssl.ca.location': '/python/sya/ca.pem',  # Path to the CA certificate
        'key.deserializer': avro_key_deserializer,
        'value.deserializer': avro_value_deserializer,
        'group.id': 'finance-syariah-group',
        'client.id': 'streaming-department-syariah',  # Set client ID to "data-streaming"
        'auto.offset.reset': "earliest"
    }

    consumer = DeserializingConsumer(consumer_conf)
    topic = "finance-syariah"
    consumer.subscribe([topic], on_assign=reset_offset)

    try:
        while True:
            # Read a single message at a time
            msg = consumer.poll(1.0)
            if msg is None:
                print(datetime.now(), "Waiting for message...")
                continue
            if msg.error():
                print("Error reading message: {}".format(msg.error()))
                continue

            # Deserialized message key and value
            key = msg.key()
            value = msg.value()

            # Handle cases with missing or None values
            if value is None:
                continue

            # Access headers if they exist within the value payload
            headers = value.get('headers', {})
            operation = headers.get("operation", "No operation found")

            # Get partition and offset
            partition = msg.partition()
            offset = msg.offset()

            # Print the message key, value, operation, partition, and offset
            print("Key:", key, "Value:", value, "Operation:", operation,
                  "Partition:", partition, "Offset:", offset)

    except Exception as ex:
        print("Kafka Exception: {}".format(ex))
    except KeyboardInterrupt:
        print("Kafka Interrupted")
    finally:
        print("Closing consumer")
        consumer.close()

