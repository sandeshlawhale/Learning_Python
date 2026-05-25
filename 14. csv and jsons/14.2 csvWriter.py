# This file explains how to use csv.writer() to write data into a CSV file.

import csv
import os

os.chdir('.\\14. csv and jsons')

# Open CSV file in write mode
file = open('output.csv', 'w', newline='')

# Create writer object
csvWriter = csv.writer(file)

# Write a single row
csvWriter.writerow(['Name', 'Age', 'City'])

# Write multiple rows
csvWriter.writerow(['Sandesh', '21', 'Nagpur'])
csvWriter.writerow(['Rahul', '22', 'Pune'])

# Close the file
file.close()

print('Data written successfully.')