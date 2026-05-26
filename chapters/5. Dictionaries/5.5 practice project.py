stuff = {"rope": 1, "torch": 6, "gold coin": 42, "arrow": 12, "dagger": 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display(inv):
    print("Inventory: ")
    item_total = 0

    for k, v in inv.items():
        print(str(v) +": "+ k)
        item_total += v

    print("total items in your inventory is ", item_total)

def addToInverntory(stuff, dragonLoot):
    for item in dragonLoot:
        stuff.setdefault(item, 0)
        stuff[item] += 1

addToInverntory(stuff, dragonLoot)
display(stuff)