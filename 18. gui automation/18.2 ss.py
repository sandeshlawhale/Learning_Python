# This file explains working with screenshots.

import pyautogui

# Take screenshot
screenshot = pyautogui.screenshot()

# Save screenshot
screenshot.save('screenshot.png')

print('Screenshot saved.')

# Analyze screenshot
pixelColor = screenshot.getpixel((100, 100))

print('Pixel Color at (100,100):', pixelColor)