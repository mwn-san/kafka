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

def calculate_time_to_consume_messages(total_messages, messages_per_interval, interval_duration):
    throughput_per_second = messages_per_interval / interval_duration
    total_seconds = total_messages / throughput_per_second
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) / 60)
    return hours, minutes

