# When python encounters an error. 
# it produces a treasure trove of errors information called the traceback.
# the traceback includes the error messages, the line number that caused that error.


# example: 
# Traceback (most recent call last):
#   File "c:\Learn Python\10. debugging\10.1 raisingException.py", line 11, in <module>
#     raise Exception('This is an error message!')                                              # this raise exception will terminate the program with the given message
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Exception: This is an error message!

# from the above example you can see that, error happenned:
#     - in 10.1 file
#     - in line 11
#     - and caused by this one 'raise Exception('This is an error message!')'open


# we can also store the traceback to a file instead of stopping our program with the help of traceback module 

import os, traceback

os.chdir('.\\10. debugging')

try:
    raise Exception('this is and error message!')
except: 
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('traceback is noted in the errorInfo file and program will be continued.')