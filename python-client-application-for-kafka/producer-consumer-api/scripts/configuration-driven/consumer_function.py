from confluent_kafka import Consumer, KafkaError, KafkaException
from kafka import KafkaAdminClient, errors
import json

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def check_topic_exists(broker, topic):
    admin_client = KafkaAdminClient(bootstrap_servers=broker)
    try:
        topic_metadata = admin_client.describe_topics([topic])
        return True
    except errors.UnknownTopicOrPartitionError:
        return False
    except Exception as e:
        print(f"Error checking topic {topic}: {e}")
        return False

def consume_messages(config_file):
    config = load_config(config_file)
    broker = config['bootstrap_servers']
    group = config['group_id']
    topic = config['topic']
    auto_offset_reset = config['auto_offset_reset']

    if not check_topic_exists(broker, topic):
        print(f"Topic {topic} does not exist.")
        return

    c = Consumer({
        'bootstrap.servers': broker,
        'group.id': group,
        'client.id': topic,
        'auto.offset.reset': auto_offset_reset
    })

    c.subscribe([topic])

    try:
        while True:
            msg = c.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            message = json.loads(msg.value().decode('utf-8'))
            print(f'Received message: {message}')
    except KafkaException as e:
        print(f"Kafka exception: {e}")
    finally:
        c.close()
