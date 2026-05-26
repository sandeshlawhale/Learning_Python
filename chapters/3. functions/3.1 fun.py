# function is like a mini program within a program
import random


# def statement                                     
def hello():                                # This mean the decleration of the function, this will not run the function
    print("hello there")
# hello()                                   # this is the call of a function, this rill run the function 


# def with parameter
def greet(name):                            # function with parameters
    print("hello " + name + "!")
# name = input()
# greet(name)                                 # function call with parameter


# with return statements
# when a function returns a value as output is a return value function, eg, len()
# what ever value we are returning from the function is return value, for this we have to use return keyword inside the fun 

def getFortune(num) :
    if num == 1:
        return "It is Certian"
    elif num == 2:
        return "It is decidely so"
    elif num == 3:
        return "Ask again later"
    elif num == 4:
        return "Outlook not so good"
    else :
        return "very doubtful"

r = random.randint(1, 5)
fortune = getFortune(r)
print("your current fortune says " + fortune)