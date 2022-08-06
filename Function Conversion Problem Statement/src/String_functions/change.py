import sys


def change(str, substring, replacement):
    return replace(str, substring, replacement)


print(change(sys.argv[1],sys.argv[2], sys.argv[2]))
