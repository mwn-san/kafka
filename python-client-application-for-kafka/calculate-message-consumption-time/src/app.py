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

from flask import Flask, render_template, request, jsonify
from function_consumer_lag_time import calculate_time_to_consume_messages

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    hours, minutes = calculate_time_to_consume_messages(int(data['total_messages']), int(data['messages_per_interval']), int(data['interval_duration']))
    return jsonify({'hours': hours, 'minutes': minutes})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)
