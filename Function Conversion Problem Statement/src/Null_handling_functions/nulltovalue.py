import sys


def null_to_value(obj, value):
    return value if isNull(obj) else obj


print(null_to_value(sys.argv[1],sys.argv[2]))
