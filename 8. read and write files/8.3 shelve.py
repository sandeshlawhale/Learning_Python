# shelve module is use to save variables in your python programs to binary shelf
# this way, your program can restore datat to variables from teh hard drive.
# the shelve module will let you  add save and open features to your program


import shelve

shelfFile = shelve.open('8. read and write files\\sample\\mydata')
cats = ['zophie', 'pooke', 'simon']
shelfFile['Cats'] = cats

print('type of shelve file :', type(shelfFile))
print('\ncontents :', shelfFile['Cats'])

print('\nkeys in shelve file :', list(shelfFile.keys()))                    # we can use all the methods from dictionary in the shelve file
print('values in shelve file :', list(shelfFile.values()))

shelfFile.close()
