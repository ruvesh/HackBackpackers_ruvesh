import sys


def field(str1, split_character, field_number):
    str_list = split(str1, split_character)
    return str_list[field_number-1]


print(field(sys.argv[1], sys.argv[2], sys.argv[3]))
