# amerDatesFile.py - this program creates a file in sample project with the name as american style date for the next program
# american date format - MM-DD-YYYY

import os
os.chdir('.\\9. organizing files')

from datetime import datetime

currentDate = datetime.now()
formatedDate = currentDate.strftime(r'%m-%d-%Y')
newFile = open('sample\\file_%s.txt' % (formatedDate), 'w')
newFile.write("%s the OG" % (formatedDate))
newFile.close()