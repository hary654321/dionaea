from datetime import datetime

current_time = datetime.now()
time_format = "%Y-%m-%d %H:%M:%S.%f"

current_time_str = current_time.strftime(time_format)
print(current_time_str)
