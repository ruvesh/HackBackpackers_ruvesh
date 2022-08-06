import sys

def get_date_from_day_since_2(days_to_add, baseline_date):
    return addDays(toDate(days_to_add), days_to_add)


print(get_date_from_day_since_2(sys.argv[1], sys.argv[2]))