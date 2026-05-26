# This file explains:
# 1. Pause and fail-safe
# 2. Mouse movement
# 3. Mouse position
# 4. controlling mouse interaction.

# Install PyAutoGUI
# Run this command in terminal:

# pip install pyautogui

import pyautogui

print('PyAutoGUI installed successfully.')

# Pause after every PyAutoGUI function call
pyautogui.PAUSE = 1

# Enable fail-safe
# Move mouse to top-left corner to stop program
pyautogui.FAILSAFE = True

# Get screen resolution
screenWidth, screenHeight = pyautogui.size()

print('Screen Width:', screenWidth)
print('Screen Height:', screenHeight)

# Move mouse to coordinates
pyautogui.moveTo(500, 300, duration=2)

# Move mouse relative to current position
pyautogui.moveRel(100, 50, duration=1)

# Get current mouse position
mouseX, mouseY = pyautogui.position()

print('\nMouse Position:')
print(mouseX, mouseY)



# Left click
pyautogui.click(500, 300)

# Double click
pyautogui.doubleClick(500, 300)

# Right click
pyautogui.rightClick(500, 300)

# Drag mouse
pyautogui.dragTo(700, 300, duration=2)

# Scroll mouse
pyautogui.scroll(500)

print('\nMouse actions completed.')