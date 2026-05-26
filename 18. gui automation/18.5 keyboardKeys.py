# This file explains keyboard control using PyAutoGUI.

import pyautogui

# Type string
pyautogui.write('Hello World!', interval=0.1)

# Press special key
pyautogui.press('enter')

# Hold and release key
pyautogui.keyDown('shift')

pyautogui.press('a')

pyautogui.keyUp('shift')

# Hotkey combination
pyautogui.hotkey('ctrl', 's')

print('Keyboard actions completed.')