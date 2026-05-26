# list is a value that contains multiple values in an ordered sequence
# spam = [4, 2, 'string', 53.0] is a list named spam
 
# values inside the list are called items
# 4 , 2 and any other values inside list are known as items from spam

spam = ['cat', 'rat', 'bat', 'elephant']


# 1. Getting values from List
# list starts with the 0th index
print("first element of list: ", spam[0])
print("third element of list: ", spam[2])
print("last element of list: ", spam[-1])           # -1 denotes to the last element from the list, and -2 is second last and so on...


# 2. list can also contatin another list called as multi dimentional list
eggs = [['cat', 'bat'], [10, 20, 30 , 40]]
print("first element in list: ", eggs[0])
print("first element in a list of list: ", eggs[0][0])


# 3. Sublist with slice
# this takes two argument start and end index, (it does not include the last index, till the element before the last index)
# you can keep the index empty, if you keep the first index empty it starts from 0 and if you keep last empty it goes till end

print("Spam Slice from 1 - 3 ", spam[1:3])
print("Spam Slice from start - 3 ", spam[:3])
print("Spam Slice from 1 - end ", spam[1:])


# 4. length of list, len()
print("length of a list is: ", len(spam))


# 5. updating values in a list
spam[1] = 'Giraffe'
print("updated the rat to giraffe: ",spam)
eggs[0][1] = 'rat'
print("updated the eggs: ",eggs)


# 6. removing value from list, del()
del spam[1]
print("can you find the giraffe: ", spam)


# 7. "in" and "not in" in list 
print("is cat in spam: ", "cat" in spam) 
print("is cat in eggs: ", "cat" in eggs) 
print("is cat in eggs[0]: ", "cat" in eggs[0]) 


# 8. multiple assignment
name1, name2, name3 = spam
print("what are name1, 2 and 3: ", name1, name2, name3)