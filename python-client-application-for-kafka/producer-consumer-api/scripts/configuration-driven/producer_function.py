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

from confluent_kafka import Producer
import json
import random
import time

def random_string(choices):
    return random.choice(choices)

def random_zipcode():
    return random.randint(10000, 99999)

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def produce_messages(config_file):
    config = load_config(config_file)
    bootstrap_servers = config['bootstrap_servers']
    topic = config['topic']
    num_messages = config['num_messages']

    p = Producer({'bootstrap.servers': bootstrap_servers})

    def delivery_report(err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    item_ids = config['item_ids']
    names = config['names']
    cities = config['cities']
    states = config['states']

    for _ in range(num_messages):
        orderid = random.randint(1, 1000000)
        message = {
            'ordertime': int(time.time()) + random.randint(-100000, 100000),
            'orderid': orderid,
            'itemid': random_string(item_ids),
            'price': round(random.uniform(99000, 25000000), 2),
            'name': random_string(names),
            'city': random_string(cities),
            'state': random_string(states),
            'zipcode': random_zipcode()
        }
        p.produce(topic, key=str(orderid), value=json.dumps(message), callback=delivery_report)
        p.poll(1)

    p.flush()
