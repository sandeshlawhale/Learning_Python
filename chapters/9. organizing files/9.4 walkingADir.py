# walkingADir.py - walk method walks thorugh all the folders and files on a give path

import os

os.chdir('.\\9. organizing files')

for folderName, subfolders, filenames in os.walk('.'):              
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName +': '+subfolder)
    
    for filename in filenames:
        print('FILE INSIDE ' + folderName +': '+filename)

    print()
