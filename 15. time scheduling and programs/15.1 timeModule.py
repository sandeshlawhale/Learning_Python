# This file explains the time module in Python.
# Topics covered:
# 1. time.time()
# 2. time.sleep()
# 3. Rounding numbers

import time

# time.time() returns current Unix timestamp
currentTime = time.time()

print('Current Timestamp:', currentTime)

# Rounding the timestamp
print('Rounded Timestamp:', round(currentTime))

# Pause the program for 3 seconds
print('\nProgram starts sleeping...')
time.sleep(3)

print('Program woke up after 3 seconds.')