import sys

def get_timet_from_timestamp(timestamp):
    time_in_millis = toLong(currentUTC() - toTimestamp(timestamp, 'yyyy-MM-dd HH:mm:ss.SSS')) * 1000L
    return time_in_millis


print(get_timet_from_timestamp(sys.argv[1]))