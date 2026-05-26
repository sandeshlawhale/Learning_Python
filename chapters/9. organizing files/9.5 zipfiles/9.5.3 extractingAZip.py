# extractAZip.py - extracts the content of the pre existing zip file

# run the 9.5.1 to create a zip file first

import zipfile, os

os.chdir('.\\9. organizing files\\9.5 zipfiles')

examplezip = zipfile.ZipFile('new.zip')
examplezip.extractall()                     # you can add path in the extractall(path) to specify the extraction folder
examplezip.close()