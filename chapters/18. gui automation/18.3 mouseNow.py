# Project: Mouse Position and RGB Color Tracker
# This program continuously displays:
# 1. Mouse X and Y coordinates
# 2. RGB color of pixel under cursor

import pyautogui

print('Press Ctrl + C to quit.\n')

try:

    while True:

        # Get mouse coordinates
        x, y = pyautogui.position()

        # Get RGB color at mouse position
        pixelColor = pyautogui.screenshot().getpixel((x, y))

        # Print data on same line
        positionStr = (
            'X: ' + str(x).rjust(4) +
            ' Y: ' + str(y).rjust(4) +
            ' RGB: ' + str(pixelColor)
        )

        print(positionStr, end='')

        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:

    print('\nDone.')