birthdays = {"alice": "jan 1",  "bob": "feb 2", "charli": "mar 3"}

while True:
    print("Enter the name(enter nothing to quit):")
    name = input()

    if name == "":
        break

    if name in birthdays:
        print(name, "birthday is on", birthdays[name])
    else :
        print("I don't have the information about ", name)
        print("Enter his birthdate(mmm d/dd): ")
        date = input()
        birthdays[name]=date
        print("DB updated!")

