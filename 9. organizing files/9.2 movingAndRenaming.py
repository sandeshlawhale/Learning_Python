# we have already created the example file and the sample folder we will be working on that here i.e. moving and renaming

import shutil, os

os.chdir('.\\9. organizing files')

# shutil.move('example.txt', 'sample')              # moving to another dir
# the above command will give an error as we already have an example file in the sample folder
# this works just like the copy but it removes the file from its source and paste it in the destination

shutil.move('example.txt', 'bacon')                # this will rename the file as we have no folder named bacon


# now we can try to move this
shutil.move('bacon', 'sample')

# rename again to example.txt and move to outside
shutil.move('sample\\bacon', 'sample\\example.txt')
shutil.move('sample\\bacon.txt','example.txt')                