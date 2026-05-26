# dictionary is  a collection of many values, but unlike indexes for lists, index fro dictornaries cn use many different data types not just integers

myCat = {"size": "fat", "color":"gray", "disposition": "loud"}
print("my cat is", myCat['size'])
print("my cat has", myCat['color'], "fur")


# keys(), values() and items()
spam = {"color": "red", "age": 42}          # color and age is keys, red and 42 are the values, combined called as item

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

for k, v in spam.items():
    print(k, v)



# exists or not in dictionary using "in" or "not in" 
print("name in spam", 'name' in spam)
print("age in spam", 'age' in spam)
print("age not in spam", 'age'not  in spam)
print("42 in spam value", 42 in spam.values())



# get() method
print("color is", spam.get("color", "black"))                   # get method return the value of the key if exists if not the returns the callback
print("limit is", spam.get("limit", 0))


# setdefault() mehtod
# this method sets the default value for the key if not present (for the first time)

print()
spam.setdefault('limit', 10)
print("what's the limit", spam['limit'])
spam.setdefault("limit", 20)
print("what's the limit", spam['limit'])
spam['limit']=20
print("what's the limit", spam['limit'])
print()                                                         # for new line


# pretty print
import pprint                                                   # this should be on top of the file

message = "today is the lovely day in Narkhed"
count={}

for c in message:
    count.setdefault(c, 0)
    count[c] += 1

print("without pretty print")
print(count)
print()

print("with pretty print")
pprint.pprint(count)

