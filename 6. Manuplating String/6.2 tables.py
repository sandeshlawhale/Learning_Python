
def printPicnicItems(item, lwidth, rwidth) :
    print("PICNIC ITEMS".center(lwidth+rwidth, '-'))

    for k, v in item.items():
        print(k.ljust(lwidth,'.') + str(v).rjust(rwidth))
    
    print()

picnicItems = {"sandwitches": 4, "apples": 32, "cups": 4, "cookies": 800}

printPicnicItems(picnicItems, 20, 6)
printPicnicItems(picnicItems, 12, 5)

