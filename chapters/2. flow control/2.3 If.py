# in flow control statements there are 2 main things
# 1. condition        -> decides weather the code block will execute or not
# 2. code block       -> actual code block we will run based on conditions

# syntax
# if condition :
#     code block
# elif condition :
#     another code block
# else:
#     last code block that will execute if the above all conditions are false

print("Enter your name: ")
name = input()

if name != "your name":
    print("sometimes things are easier than you think")
else :
    print("you got it")