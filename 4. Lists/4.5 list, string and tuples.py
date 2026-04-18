# we can handle the strings same as the list

eggs = "chicken"
print(eggs[4])
print(eggs[4:])

for i in eggs:
    if i == " ":
        continue
    print("* * *" + i + "* * *")



# mutable and immutable
# list are mutable but strings are not
# we cannot update the values in string instead we can make new string with the help of slice

sussy = eggs[:5]
print("what are sussy?", sussy)

spam = [1, 2, 3]
pool = spam
pool = [4, 5, 6]
print("what are spam: ", spam)
print("what are pool: ", pool)

spam = [7, 8, 9]
print("what are spam: ", spam)


# tuple, () instead of []
# tuple is almost identicle to the list but it is immutable
# same methods can be perfomed as list

box = ("hello", 42, 53.0)
print(box[0], box[1:])

# box[0] ="hi"                      # this will cause an error as the tuple is immutable


# converting types with list() and tuple() function
pages = list(box)
print("pages", pages)
pages = tuple(pages)
print("pages", pages)


# reference 
cheese = spam
cheese[1] = "hello"
print("cheese", cheese)
print("spam", spam)

# copy module copy() and deepcopy()
import copy         # this should be at the top of page

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)                            # this is copy of the original, used when you dont want to alter original
cheese[1] = 1
print("cheese", cheese)
print("spam", spam)
