# Project: Super Stopwatch
# This program tracks the amount of time between Enter key presses.
# It prints:
# 1. Lap number
# 2. Total elapsed time
# 3. Lap time

import time

print('Press ENTER to begin.')
input()

print('Started.')
print('Press ENTER to record lap time.')
print('Press Ctrl + C to quit.\n')

# Store starting time
startTime = time.time()

# Store last lap time
lastTime = startTime

# Lap counter
lapNum = 1

try:

    while True:

        input()

        # Current time
        lapTime = round(time.time() - lastTime, 2)

        # Total elapsed time
        totalTime = round(time.time() - startTime, 2)

        # Print lap information
        print('Lap #' + str(lapNum) +
              ': ' + str(totalTime) +
              ' (' + str(lapTime) + ')')
        

        # Reset last lap time
        lastTime = time.time()

        # Increment lap number
        lapNum += 1

except KeyboardInterrupt:

    # Handle Ctrl + C
    print('\nDone.')