# This file explains the datetime module and timedelta data type.

import datetime

# Current date and time
currentDate = datetime.datetime.now()

print('Current Date and Time:')
print(currentDate)

# Create custom datetime object
customDate = datetime.datetime(2026, 5, 25, 10, 30, 0)

print('\nCustom Date:')
print(customDate)

# Access individual attributes
print('\nYear:', customDate.year)
print('Month:', customDate.month)
print('Day:', customDate.day)

# timedelta object
delta = datetime.timedelta(days=7, hours=5)

print('\nTimedelta:')
print(delta)

# Add timedelta to datetime
futureDate = currentDate + delta

print('\nFuture Date:')
print(futureDate)