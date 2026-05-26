# This file explains image recognition using PyAutoGUI.

import pyautogui
import os

os.chdir('.\\18. gui automation')

# Locate image on screen
location = pyautogui.locateOnScreen('tab.png', confidence=0.8)

print('Image Location:')
print(location)

# Click center of image
if location != None:

    center = pyautogui.center(location)

    pyautogui.click(center)

    print('Button clicked.')

else:

    print('Image not found.')