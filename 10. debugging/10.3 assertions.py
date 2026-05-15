# An assertion is a sanity check to make sure your code is not doing something obviously wrong.

# is consists of:
#     - the assert keyword
#     - a conditions 
#     - a comma
#     - a string to display when the condition is false

podBayDoorStatus = 'open'

assert podBayDoorStatus != 'open', 'The pod bay doors need to be open.'
