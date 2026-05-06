# shutil (shell utilities) - lets you copy, move, rename, and delete files inyour py program


import shutil, os

os.chdir('.\\9. organizing files')

exampleFile = open('example.txt', 'w')                      # this automatically creates the file in cwd
exampleFile.write('example file that we will be moving in the another folder')
exampleFile.close()

# shutil.copy('example.txt', 'sample.txt')                  # this copies the data from example file to sample file, if not exist the it creats new
shutil.copy('example.txt', 'sample')                        # this copies the data from example file to example file in sample folder as we dont specify the name of the copied file
shutil.copy('example.txt', 'sample\\example-copy.txt')      # we specified the new name for the copied file

