import datetime
def get_clock(hour, minute, second=0):
    hour = hour % 12
    hour_angle = 30 * hour + 0.5 * minute + second * (0.5 / 60)
    minute_angle = 6 * minute + 0.1 * second
    diff = abs(hour_angle - minute_angle)
    return min(diff, 360 - diff)
#TODO SPRAWDZIC KTORY WYNIK JEST DOBRY

def get_clock_angles_from_datetime(dt):
    h = dt.hour % 12
    m = dt.minute
    s = dt.second
    hour_angle = 30 * h + 0.5 * m + s * 0.5/60
    minute_angle = 6 * m + 0.1 * s
    seconds_angle = 6 * s
    return {"hour_minute": angle_diff(hour_angle, minute_angle),
            "hour_seconds": angle_diff(hour_angle, seconds_angle),
            "minute_seconds": angle_diff(minute_angle, seconds_angle)}

def angle_diff(a, b):
    diff = abs(a - b)
    return min(diff, 360-diff)

def main():
    now = datetime.datetime.now()
    print(get_clock(now.hour, now.minute))
    print(get_clock_angles_from_datetime(now))

if __name__ == "__main__":
    main()