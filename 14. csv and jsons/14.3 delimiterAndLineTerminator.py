# This file explains delimiter and line terminator keyword arguments in csv.writer().

import csv
import os

os.chdir('.\\14. csv and jsons')

# Open CSV file in write mode
file = open('delimiter_example.csv', 'w', newline='')

# Create writer object with custom delimiter and line terminator
csvWriter = csv.writer(file, delimiter='|', lineterminator='\n\n')

# Write rows into CSV file
csvWriter.writerow(['Name', 'Age', 'City'])
csvWriter.writerow(['Sandesh', '21', 'Nagpur'])
csvWriter.writerow(['Rahul', '22', 'Pune'])

# Close the file
file.close()

print('CSV file created with custom delimiter and line terminator.')