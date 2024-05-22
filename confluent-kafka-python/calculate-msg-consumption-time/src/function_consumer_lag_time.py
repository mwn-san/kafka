def calculate_time_to_consume_messages(total_messages, messages_per_interval, interval_duration):
    throughput_per_second = messages_per_interval / interval_duration
    total_seconds = total_messages / throughput_per_second
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) / 60)
    return hours, minutes

