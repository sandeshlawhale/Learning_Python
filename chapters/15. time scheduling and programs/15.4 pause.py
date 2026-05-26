# This file explains:
# 1. Pausing until a specific date
# 2. Converting datetime object into string
# 3. Converting string into datetime object

import datetime
import time

# Future date and time
futureDate = datetime.datetime(2026, 1, 1, 0, 0, 0)

print('Waiting until:', futureDate)

# Pause until future date
while datetime.datetime.now() < futureDate:
    time.sleep(1)

print('Reached the target date.')

# Convert datetime object into string
now = datetime.datetime.now()

dateString = now.strftime('%Y/%m/%d %H:%M:%S')

print('\nDatetime converted into string:')
print(dateString)

# Convert string into datetime object
stringDate = '2026/05/25 10:30:00'

datetimeObject = datetime.datetime.strptime(
    stringDate,
    '%Y/%m/%d %H:%M:%S'
)

print('\nString converted into datetime object:')
print(datetimeObject)