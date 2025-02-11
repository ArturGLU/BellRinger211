import datetime

def hours():
    current_time = datetime.datetime.now()
    valentines_day = datetime.datetime(current_time.year, 2, 14, 0, 0, 0)

    if current_time >= valentines_day:
        valentines_day = datetime.datetime(current_time.year + 1, 2, 14, 0, 0, 0)

    time_difference = valentines_day - current_time
    hours_remaining = time_difference.total_seconds() / 3600

    return round(hours_remaining, 2)

print("Number of hours left: " + str(hours()))
