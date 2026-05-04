# Call the open() function to return a file obj
# Calll the read() or write() method on the file obj
# close the file by calling close() method on the file obj


# opening and reading a file  ----------------------------------------->
sampleFile = open('8. read and write files\\sample\\sampleFile.txt')
sampleFileContent = sampleFile.read()
print("content form sample file:", sampleFileContent)
sampleFile.close()


# readlines() method  ----------------------------------------->
# to get all the lines as a list 
multilineFile = open('8. read and write files\\sample\\multiline.txt')
multilineContent = multilineFile.readlines()
print("\ncontent form sample file as list:", multilineContent)
multilineFile.close()


# writing to files - w  ----------------------------------------->
baconFile = open('8. read and write files\\sample\\sampleFile.txt', 'w')                    # this w indicates the write mode, replaces the old text
baconFile.write('changing the sample file to bacon content!\n')
baconFile.close()


# append to files - a  ----------------------------------------->
baconFile = open('8. read and write files\\sample\\sampleFile.txt', 'a')                    # this a indicates the append mode, this does not replaces the old text it add new while keeping the old one
baconFile.write('appending the new text in sample file\n')
baconFile.close()


# reading from files - a  ----------------------------------------->
baconFile = open('8. read and write files\\sample\\sampleFile.txt', 'r')                    # this r indicates the read mode, this mode is default we have no need to specify here
print('\ncontent from the sample file after changing:', baconFile.read())
baconFile.close()

