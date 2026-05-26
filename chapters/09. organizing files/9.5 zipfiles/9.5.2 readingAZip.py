# readingAZip.py - reads the zip file that exisits

# run the 9.5.1 to create a zip file first

import zipfile, os

os.chdir('.\\9. organizing files\\9.5 zipfiles')

examplezip = zipfile.ZipFile('new.zip')
content = examplezip.namelist()
print("content in zip file : "+ str(content))


contentInfo = examplezip.getinfo('../example.txt')
print("filesize of file inside the zip file: " + str(contentInfo.file_size))                        # in bytes
print("compress size of file inside the zip file: " + str(contentInfo.compress_size))