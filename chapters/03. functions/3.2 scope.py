# there are two types of scope in python
# local scope and global scope

# varaible and parameters that are assigned in a called fucntion are said to exist in that funcation's local scope/
# and variables that are assigned outside all func tions are said to exists in the global scope

# def sapm():
    # eggs = 42
# print(eggs)           # if you run this it will cause an error cause this eggs has the local scope from above fun


ham = 0
def spam():
    eggs = 99
    bacon()
    print("eggs: ", eggs)

def bacon():
    global ham          # with global keyword we can access the global varaible
    ham = 101
    eggs = 0            # this will not change as this variable has the local scope from the other fun

spam()
print("ham: ", ham)
