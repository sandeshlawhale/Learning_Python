# python has some built in funtions but python also comes with a set of modules called the standard liabrary


# syntax
# import module_name

import random, sys

for i in range(0, 5):
    print("i : ", random.randint(1, 100))

while True:
    print("Type exit to exit")
    res = input()
    if res == 'exit':
        sys.exit()
    print("You typed " + res + ", can't you even type exit")