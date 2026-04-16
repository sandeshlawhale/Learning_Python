# exception handling is used to prevent the unwanted carshing of the program
# this is done with the help of try and catch keyword


def spam(divideby): 
    try:                                                            # this block runs the code that might contain error
        return 42/divideby
    except ZeroDivisionError:                                       # this block catches that error and excutes this command instead of crashing
        print("Error: invalid arguments, zero not allowed")            

print(spam(2))
print(spam(0))
print(spam(42))
