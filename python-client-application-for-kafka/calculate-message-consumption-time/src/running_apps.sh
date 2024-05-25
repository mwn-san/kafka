#!/bin/bash
source venv/bin/activate
nohup sh -c 'python3 app.py > output.log 2>&1' &
