# This file explains multithreading in Python.
# Topics covered:
# 1. Multithreading
# 2. Passing arguments to threads
# 3. Target function
# 4. Concurrency issues

import threading
import time

# Target function for thread
def printNumbers(name, delay):

    for i in range(5):

        print(name, '->', i)

        # Pause thread
        time.sleep(delay)

# Create threads
thread1 = threading.Thread(target=printNumbers, args=('Thread-1', 1))

thread2 = threading.Thread(target=printNumbers, args=('Thread-2', 2))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print('\nAll threads finished.')

# Concurrency Issue:
# Multiple threads accessing same data at same time
# can cause unexpected results.