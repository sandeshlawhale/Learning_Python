import zipfile, os

os.chdir('.\\9. organizing files\\9.5 zipfiles')

# first run the 9.1 to create a example.txt file

newzip = zipfile.ZipFile('new.zip', 'w')                                        # this creates the zip file named new.zip in a write mode
newzip.write('..\\example.txt', compress_type=zipfile.ZIP_DEFLATED)             # this writes the content in the zip file, we have added the example.txt file and compress type as zip defaulted
newzip.close()                                                                  # close the zip 


    # after this we can see a new.zip file in our dir