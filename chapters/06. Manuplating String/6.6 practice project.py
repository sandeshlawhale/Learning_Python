# table print

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['ALICE', 'BOB', 'CAROL', 'DAVID'],
    ['Dogs', 'Cats', 'Moose', 'goose'],
]

columnWidth = [0] * len(tableData)

for i in range(len(tableData)):
    for item in tableData[i] :
        if len(item) > columnWidth[i]:
            columnWidth[i] = len(item)

def printTable(data) :
    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].rjust(columnWidth[j]), end="  ")
        print()



printTable(tableData)
# print(columnWidth)