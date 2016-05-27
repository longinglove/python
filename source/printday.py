#!/usr/bin/env python

months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
]

endings = ['st', 'nd', 'rd'] + 17*['th'] + ['st', 'nd', 'rd'] + 7*['th'] + ['st']

year = raw_input('Year: ')
month = raw_input('Month(1-12): ')
day = raw_input('Day(1-31): ')

month_number = int(month) - 1
day_number = int(day) - 1

month_name = months[month_number]
day_name = day + endings[day_number]

print month_name + ' ' + day_name + ', ' + year
