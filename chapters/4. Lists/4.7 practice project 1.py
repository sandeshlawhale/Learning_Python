# comma code


spam = []

while True:
    print("enter a value (enter none to stop): ")
    name = input()

    if name == "":
        break

    spam.append(name)

for i in range(0, len(spam)):
    if i == len(spam) -1:
        print("and " + spam[i], end="")
    else:
        print(spam[i] + ", ", end="")