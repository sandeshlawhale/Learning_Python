# deleteAZip.py - this is a cleanup file that removes the zip and extracted file in the end

import os

os.chdir('.\\9. organizing files\\9.5 zipfiles')


for filename in os.listdir():
    if filename.endswith(('.txt', '.zip')):
        print(filename)
        os.unlink(filename)