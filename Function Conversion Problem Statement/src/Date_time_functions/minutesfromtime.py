import sys

def get_minutes_from_time(time):
    return minute(toTimestamp(time, 'HH:mm:ss.SSS'))


print(get_minutes_from_time(sys.argv[1]))