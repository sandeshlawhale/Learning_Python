# renameDates.py - renames filenames with american mm-dd-yyyy format to european dd-mm-yyyy format

import shutil, os, re
os.chdir('.\\9. organizing files')

dateRegex = re.compile(r""" 
    ^(.*?)                          # any name in the start before date
    ((0|1)?\d)-                     # month
    ((0|1|2|3)?\d)-                     # day
    ((19|20)?\d\d)                      # year
    (.*?)$                          # any name or ext after date
""", re.VERBOSE)


# loop over files in working dir
for amerFileName in os.listdir('.\\sample'):
    mo = dateRegex.search(amerFileName)

    # skip files without a date
    if mo == None:
        continue

    # get teh different parts of the filename
    startName = mo.group(1)
    extName = mo.group(8)
    day = mo.group(4)
    month = mo.group(2)
    year = mo.group(6)

    # form the european style filename
    euroFileName = startName + day + "-" + month + "-" + year + extName

    # get the full, aboslute file paths. 
    abswd = os.path.abspath('.\\sample')
    amerFileName = os.path.join(abswd, amerFileName)
    euroFileName = os.path.join(abswd, euroFileName)

    # rename the files.
    print('renaming %s to %s' % (amerFileName, euroFileName))
    shutil.move(amerFileName, euroFileName)
