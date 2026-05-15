# Python raises an exception whenever it tries to execute invalid code 
# but we can also raise your own exceptions in your code


# To raise an exceptions,
#     - The raise keyword
#     - A call to the Exception() function
#     - a string with a helpful error message passed to the exception() function


# raise Exception('This is an error message!')                                              # this raise exception will terminate the program with the given message


def boxPrint(sy, w, h):
    if len(sy) != 1:
        raise Exception('Symbol must be a single character string.')            # we use the raise exception to tell the user our requirments
    if w <=2:
        raise Exception('Width must be greater than 2')
    if h <=2:
        raise Exception('Height must be greater than 2')
    
    print(sy * w)
    for i in range(h-2):
        print((sy + (" " * (w -2)) + sy))
    print(sy * w)


for sy, w, h in (("*", 4, 4), ('0', 20, 5), ('x', 1, 3), ('zz', 2, 4)):
    try:                                                                    # we dont want to halt the program after an exception that is why we used the try excep block to make sure the programs runs smoothly while showing the problem
        boxPrint(sy, w, h)
    except Exception as err: 
        print('An exception happenned: ' + str(err))