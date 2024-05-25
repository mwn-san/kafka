#!/usr/bin/env python
#
# Copyright 2024 Mohammad Wildan Nuryulda
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Mohammad Wildan Nuryulda
# Email: nuryulda@gmail.com
# GitHub: https://github.com/mwn-san

import logging
from logging.handlers import RotatingFileHandler
from confluent_kafka import Consumer, KafkaError, KafkaException
from kafka import KafkaAdminClient, errors
import json
import traceback

# Configure Kafka internal logging to both stdout and file
kafka_file_handler = RotatingFileHandler("consumer_kafka.log", maxBytes=100*1024*1024, backupCount=3)  # 100MB
kafka_file_handler.setLevel(logging.INFO)
kafka_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

kafka_stream_handler = logging.StreamHandler()
kafka_stream_handler.setLevel(logging.ERROR)
kafka_stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

kafka_logger = logging.getLogger('kafka')
kafka_logger.setLevel(logging.DEBUG)
kafka_logger.addHandler(kafka_file_handler)
kafka_logger.addHandler(kafka_stream_handler)

# Configure application logging to both stdout and file
app_file_handler = RotatingFileHandler("consumer_app.log", maxBytes=100*1024*1024, backupCount=3)  # 100MB
app_file_handler.setLevel(logging.DEBUG)
app_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

app_stream_handler = logging.StreamHandler()
app_stream_handler.setLevel(logging.DEBUG)
app_stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

app_logger = logging.getLogger('consumer_app_logger')
app_logger.setLevel(logging.DEBUG)
app_logger.addHandler(app_file_handler)
app_logger.addHandler(app_stream_handler)

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
        app_logger.error(f"Error checking topic {topic}: {e}")
        return False

# Don't want to check the fields in the message, you can comment this function:
#def validate_message(message):
    required_fields = ["ordertime", "orderid", "itemid", "price", "name", "city", "state", "zipcode"]
    for field in required_fields:
        if field not in message:
            return False
    return True

def consume_messages(config_file):
    config = load_config(config_file)
    broker = config['bootstrap_servers']
    group = config['group_id']
    topic = config['topic']
    auto_offset_reset = config['auto_offset_reset']

    conf = {
        'bootstrap.servers': broker,
        'group.id': group,
        'auto.offset.reset': auto_offset_reset,
        'enable.auto.offset.store': False,
    }

    if not check_topic_exists(broker, topic):
        app_logger.error(f"Topic {topic} does not exist.")
        return

    c = Consumer(conf)
    app_logger.info(f"Initialized.Consumer.With.Broker:\n{broker}\nConsumer.Group: {group}\nTopic.Name: {topic}\nAuto.Offset.Reset: {auto_offset_reset}")

    def print_assignment(consumer, partitions):
        app_logger.info('Assignment : %s', partitions)

    c.subscribe([topic], on_assign=print_assignment)

    try:
        message_count = 0
        detailed_log_limit = 1  # Limit for detailed logging of messages
        while True:
            msg = c.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                if msg.value() is None:
                    app_logger.error(f"Received tombstone (null value) message at partition {msg.partition()} offset {msg.offset()}")
                    # Uncomment the next line to stop consuming on tombstone message
                    # break
                    continue

                try:
                    message = json.loads(msg.value().decode('utf-8'))
                except json.JSONDecodeError as e:
                    app_logger.error(f"JSON decode error: {e}")
                    continue

                # Don't want to check the fields in the message, you can comment the following two lines:
                #if not validate_message(message):
                    app_logger.error(f"Invalid message format: {message}")
                    continue

                if message_count < detailed_log_limit:
                    app_logger.info("ONE OF THE MESSAGES CONSUMED IS AS FOLLOWS...")
                    app_logger.info(f"{message}")
                    app_logger.info(f"MESSAGE CONSUMED FROM  /PARTITION/ = {msg.partition()} /OFFSET/ = {msg.offset()}")
                elif message_count == detailed_log_limit:
                    app_logger.info("CONSUMING MESSAGES BEYOND THE INITIAL DETAILED LOG LIMIT.")
                
                # Print all messages to terminal
                print(f"Received message: {message} from partition: {msg.partition()} at offset: {msg.offset()}")

                message_count += 1
                c.store_offsets(msg)

    except KafkaException as e:
        app_logger.error(f"Kafka exception: {e}")
    except KeyboardInterrupt:
        app_logger.info('Consumer interrupted by user')
        app_logger.info(traceback.format_exc())
    finally:
        c.close()
