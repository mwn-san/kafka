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

from consumer_function import consume_messages

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    config_file = 'config_consumer.json'
    consume_messages(config_file)
