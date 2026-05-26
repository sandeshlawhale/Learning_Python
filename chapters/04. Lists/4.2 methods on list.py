# method is a same thing as a function but it is called on a value 

spam = ['bat', 'rat', 'cat', 'elephant']

#  1. finding value in a list, index()
print("index of bat is: ", spam.index('cat'))
# print("index of ball is: ", spam.index('ball'))                   # this will give "not in list" error

# 2. adding value in a list, insert() and append()
spam.append('giraffe')
print("can you see the giraffe? ", spam)

spam.insert(2, "ball")
print("can you find the ball?", spam)  


# 3. removing value from list, remove()
spam.remove('ball')
print("can you find the ball?", spam)  


# 4. sort the list, sort()
spam.sort()
print("can you see the difference? ", spam)