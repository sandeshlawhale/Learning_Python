# instead of doing  
#   print("enter first cate name: ")
#   catName1 = input()
# we used the list to store all cat names in organized way

catNames = []

while True:
    print("Enter the name of cat " + str(len(catNames) + 1) + (" (Enter nothing to stop!):"))
    name = input()

    if name == "":
        break

    catNames.append(name)

print("cats name are: ", catNames)