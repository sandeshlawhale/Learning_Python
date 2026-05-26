# Project: Human Like Looking Busy Program
# This program randomly moves the mouse cursor
# to random screen coordinates after random delays.

import pyautogui
import random
import time

# Get screen resolution
screenWidth, screenHeight = pyautogui.size()

print('Screen Width:', screenWidth)
print('Screen Height:', screenHeight)

print('\nHuman-like Looking Busy program started.')
print('Press Ctrl + C to stop.\n')

try:

    while True:

        # Generate random X coordinate
        randomX = random.randint(0, screenWidth - 1)

        # Generate random Y coordinate
        randomY = random.randint(0, screenHeight - 1)

        # Random movement duration
        moveDuration = round(random.uniform(0.5, 3), 2)

        # Move mouse smoothly
        pyautogui.moveTo(
            randomX,
            randomY,
            duration=moveDuration
        )

        print(
            f'Moved to ({randomX}, {randomY}) '
            f'in {moveDuration} seconds'
        )

        # Random waiting time
        waitTime = random.randint(5, 60)

        print(f'Waiting {waitTime} seconds...\n')

        # Wait before next movement
        time.sleep(waitTime)

except KeyboardInterrupt:

    print('\nProgram stopped.')