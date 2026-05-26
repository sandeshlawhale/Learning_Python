# Project: Removing the header from CSV files.
# This program finds all CSV files in the current working directory,
# reads the content of each file, removes the first row (header),
# and writes the remaining data into a new CSV file.

import csv
import os

os.chdir('.\\14. csv and jsons')

# Loop through every file in the current working directory
for csvFile in os.listdir('.'):

    # Process only CSV files
    if csvFile.endswith('.csv'):

        print('Removing header from:', csvFile)

        # Open the original CSV file
        csvRows = []

        fileObj = open(csvFile)
        readerObj = csv.reader(fileObj)

        # Loop through each row in the CSV file
        for rowIndex, row in enumerate(readerObj):

            # Skip the first row
            if rowIndex == 0:
                continue

            # Add remaining rows to csvRows list
            csvRows.append(row)

        fileObj.close()

        # Create a new CSV file without header
        newFileObj = open('noHeader_' + csvFile, 'w', newline='')

        # Create writer object
        writerObj = csv.writer(newFileObj)

        # Write rows into the new CSV file
        for row in csvRows:
            writerObj.writerow(row)

        newFileObj.close()

print('Header removed from all CSV files.')