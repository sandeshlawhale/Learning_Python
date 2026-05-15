# Instead of printing every statement in your code, use logging  to debug your python code.
# to use logging we need to import logging 

# why do we use the logging over print, is the main question, cause with one line we can dissable all logs and in print we have to do that manually
# have a look at line no, 10

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')           # this line defines the format of the loggs and it is mandatory to add those two line to make the logs work

# logging.disable()

def factorial(n):
    logging.info('Start of Program')
    total = 1
    for i in range(n+1):
    # for i in range(1, n+1):
        total*=i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.warning('End of program')

# after running the above program we will get the logs like this
#  2026-05-15 14:33:19,098 - INFO - Start of Program
#  2026-05-15 14:33:19,099 - DEBUG - i is 0, total is 0
#  2026-05-15 14:33:19,099 - DEBUG - i is 1, total is 0
#  2026-05-15 14:33:19,099 - DEBUG - i is 2, total is 0
#  2026-05-15 14:33:19,099 - DEBUG - i is 3, total is 0
#  2026-05-15 14:33:19,100 - DEBUG - i is 4, total is 0
#  2026-05-15 14:33:19,100 - DEBUG - i is 5, total is 0
#  2026-05-15 14:33:19,100 - DEBUG - End of factorial(5)
# 0
#  2026-05-15 14:33:19,100 - WARNING - End of program
# from this we can understand the range of our loop should be 1 to n+1 try runnning after updation




# logging levels
# Debug           logging.debug()             The lowest level used for small details
# INFO            logging.info()              used to recod information on general events
# Warning         logging.warning()           used to indicate a potential problem that doesn;t prevent the program from working but might do so in future 
# Error           logging.error()             used to record an error that caused the program to fail to do something
# Critical        logging.critical()          the highest level. used to indicate the fatal error




# Disabling logging
# after you have debugged you program, you need to dissable the logging so the message will not clutter in the production
# to do this we use logging.disable() functions

# see line no. 10 for disabling logging

# logging.dissable()                # dissables all logs
# logging.dissable(logging.INFO)    # dissables only info logs we can specify other levels as well