# deletingFilesAndFolders.py - learn to delete the files and folder in your python program

# os.unlink(path) - delete the file at path
# os.rmdir(path) - delete the folder at path and the folder must be empty 
# shutil.rmtree(path) - remove the folder at path and all files and folders it contains will also get deleted

import os, send2trash

os.chdir('.\\9. organizing files')

for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)                   # this code will list the file that are goint to be deleted
        # os.unlink(filename)

# this unlink method deletes the file permanently

# run 9.1 to generate the example file again


# to safe delete we use send2trash module, this keep the deleted file in the recycle bin
# this is a third party plugin to install it by - pip install send2trash
send2trash.send2trash('example.txt')


