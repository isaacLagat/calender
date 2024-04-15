

import calendar

def print_calendar(year, month):
    cal = calendar.month(year, month)
    return cal

year = 2024
month = 4
output = print_calendar(year, month)
print(output)