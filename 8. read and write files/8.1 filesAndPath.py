# a file has two key properties
# a file name - usually wriite as one word 
# and a path - specific location of a file on a computer


# backslash in path ----------------------------------------->
import os

spam = os.path.join('C:', 'user', 'learnPython', 'filesAndPath.py')
print(spam)             # this will join the dirs using proper slash like back in windows and forward in linux and others 

# cwd - current working directory ----------------------------------------->
print("cwd: ", os.getcwd())


# to change the working dir ----------------------------------------->
os.chdir('C:\\Users\\sande\\OneDrive\\Documents\\codex\\Learn Python\\8. read and write files')
print("cwd after changing: ", os.getcwd(), '\n')



# absollute and relative path ----------------------------------------->
# absolute path starts from the root dir that is usually the C:/
# relative path starts form the program's cwd

# 8. read and write files\8.1 filesAndPath.py                                       #this is the relative path
# C:\User\learnPython\8. read and write files\8.1 filesAndPath.py                   # this is the absolute path



# creating new folders with - makedirs() ----------------------------------------->
# the below command will create the new folder inside the current working folder
# os.makedirs('.\\something to test the makedirs')                                # the . represents the current working folder or cwd
                                                                                  # the .. represents the parent folder


# os.path module  ----------------------------------------->
spam = os.path.abspath('.')
print("abs path of .:", spam)
eggs = os.path.abspath('.\\8.1 filesAndPath.py')
print("abs path of .\\8.1 filesAndPath.py:", eggs)

print("is . an abs path:", os.path.isabs('.'))                                                              
print("is . an abs path after os.path.abspath? :", os.path.isabs(os.path.abspath('.')))

# same is applied for the relative paths the command is isrel and relpath



# dir name and base name ----------------------------------------->
# C:\User\learnPython\8. read and write files\8.1 filesAndPath.py

# in the above path
# dir name = C:\User\learnPython\8. read and write files
# base name = 8.1 filesAndPath.py
print()
path = 'C:\\User\\learnPython\\8. read and write files\\8.1 filesAndPath.py'
print("dir name of the path is : ", os.path.dirname(path))
print("base name of the path is : ", os.path.basename(path))
print()

# there is short hand version of the above  called as split
print("split dir and base name from path: ", os.path.split(path))

# if we need the same for each folder we can use split on path and pass the sep as arg
print("seperate at each folder st.: ", path.split(os.path.sep))


# file size and folder content  ----------------------------------------->
print("size of the current dir: ", os.path.getsize(os.path.abspath('.\\8.1 filesAndPath.py')))              #returns the size of the file or folder in bytes

# if we want to get the size of all files the we can get all files by 'os.listdir' and maping over each of them and calculating simultaneouly


# check path validity  ----------------------------------------->
print()
print("does windows folder exists in c:", os.path.exists('C:\\Windows'))                                            # we can use to check the external storage is plugged in or not
print("does soemthing_folder exists in c:", os.path.exists('C:\\soemthing_folder'))

print()
print("is cwd dir:", os.path.isdir(os.path.abspath('.')))
print("is cwd file:", os.path.isfile(os.path.abspath('.')))

