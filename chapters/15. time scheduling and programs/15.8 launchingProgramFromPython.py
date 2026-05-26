# This file explains launching other programs from Python.

import subprocess
import webbrowser

# Open website in default browser
webbrowser.open('https://python.org')

# Run another Python file
subprocess.Popen(['python', 'example.py'])

# Open text file with default application
subprocess.Popen(['start', 'sample.txt'], shell=True)

print('Programs launched successfully.')

# Task Scheduler:
# Windows tool used to schedule programs.

# launchd:
# macOS service used to schedule tasks.

# cron:
# Linux scheduler used to run scheduled tasks.