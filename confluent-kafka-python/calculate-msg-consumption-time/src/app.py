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
