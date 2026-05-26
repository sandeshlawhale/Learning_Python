# Practice Project: Prettified Stopwatch
# This program tracks lap times and prints them in a formatted way.

import time

print('Press ENTER to begin.')
input()

print('Started.')
print('Press ENTER for each lap.')
print('Press Ctrl + C to quit.\n')

# Starting time
startTime = time.time()

# Last lap time
lastTime = startTime

# Lap counter
lapNum = 1

try:

    while True:

        input()

        # Current lap time
        lapTime = round(time.time() - lastTime, 2)

        # Total elapsed time
        totalTime = round(time.time() - startTime, 2)

        # Prettified output
        print(
            'Lap #%s: %s (%s)' %
            (
                str(lapNum).rjust(2),
                str(totalTime).rjust(5),
                str(lapTime).rjust(5)
            )
        )

        # Reset last lap time
        lastTime = time.time()

        # Increase lap number
        lapNum += 1

except KeyboardInterrupt:

    print('\nDone.')
    