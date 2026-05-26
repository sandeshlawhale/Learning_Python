# Project: Automatic Form Filler
# This program automatically fills a form using keyboard and mouse automation.

import pyautogui
import time

# Wait before starting
print('Program starts in 5 seconds...')
time.sleep(5)

# Example form data
formData = [
    ['Sandesh', 'sandesh@gmail.com', 'Nagpur'],
    ['Rahul', 'rahul@gmail.com', 'Pune']
]

# Loop through data
for data in formData:

    # Click first field
    pyautogui.click(500, 300)                           # cordinates of your first field of the form, change it accordingly

    # Type name
    pyautogui.write(data[0])

    pyautogui.press('tab')

    # Type email
    pyautogui.write(data[1])

    pyautogui.press('tab')

    # Type city
    pyautogui.write(data[2])

    pyautogui.press('tab')

    # Submit form
    pyautogui.press('enter')

    print('Form submitted.')

    # Wait before next entry
    time.sleep(2)

print('All forms submitted.')