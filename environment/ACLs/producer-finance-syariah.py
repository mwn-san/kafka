import random
import time
from datetime import datetime
import pytz
from confluent_kafka.avro import AvroProducer
from confluent_kafka.avro.serializer import SerializerError
import string

# Define Avro schema for key and value
key_schema_str = """
{
   "type": "record",
   "name": "TransactionKey",
   "fields": [
       {"name": "transaction_id", "type": "string"}
   ]
}
"""

value_schema_str = """
{
   "namespace": "finance.syariah",
   "type": "record",
   "name": "Transaction",
   "fields": [
       {"name": "transaction_id", "type": "string"},
       {"name": "amount", "type": "double"},
       {"name": "currency", "type": "string"},
       {"name": "timestamp", "type": "string"}
   ]
}
"""

# Kafka configuration with SASL/SCRAM and schema registry URL
kafka_config = {
    'bootstrap.servers': '<host>:<port>',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'SCRAM-SHA-512',
    'sasl.username': 'digital',
    'sasl.password': 'confluent',
    'ssl.ca.location': '/python/sya/ca.pem',
    'schema.registry.url': 'http://<host>:<port>',
    'schema.registry.basic.auth.user.info': 'digital:confluent',
    'schema.registry.basic.auth.credentials.source': 'USER_INFO'
}

# Create AvroProducer instance with both key and value schema
avro_producer = AvroProducer(
    kafka_config,
    default_key_schema=key_schema_str,
    default_value_schema=value_schema_str
)

# Set timezone to Asia/Jakarta
jakarta_tz = pytz.timezone("Asia/Jakarta")

# Function to generate a random transaction ID with letters and numbers
def generate_transaction_id(length=16):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Generator function to create random transaction data with formatted Jakarta timestamp
def generate_transaction_data():
    while True:
        # Get current time in Jakarta timezone and format
        current_time = datetime.now(jakarta_tz)
        formatted_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

        transaction_data = {
            "transaction_id": generate_transaction_id(),
            "amount": round(random.uniform(100.0, 10000.0), 2),
            "currency": "IDR",
            "timestamp": formatted_timestamp
        }
        yield transaction_data
        time.sleep(1)  # delay to simulate streaming

# Produce messages to Kafka using the generator, with transaction_id as the key
try:
    for data in generate_transaction_data():
        transaction_id = {"transaction_id": data["transaction_id"]}  # Key schema requires a dict with transaction_id
        avro_producer.produce(topic='finance-syariah', key=transaction_id, value=data)
        avro_producer.flush()
        print(f"Sent: {data} with key: {transaction_id}")
except SerializerError as e:
    print(f"Error in sending data: {e}")
except Exception as e:
    print(f"General error in sending data: {e}")

