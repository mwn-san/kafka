def function_calculate_time_to_consume_messages(total_messages, messages_per_interval, interval_duration):
    # Menghitung throughput per detik
    throughput_per_second = messages_per_interval / interval_duration
    
    # Menghitung total waktu dalam detik
    total_seconds = total_messages / throughput_per_second
    
    # Mengonversi total detik ke jam dan menit
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) / 60)
    
    return hours, minutes
