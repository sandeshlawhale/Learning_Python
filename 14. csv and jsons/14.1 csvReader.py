# This file explains how to use csv.reader() to read data from CSV files in Python.

import csv
import os

os.chdir('.\\14. csv and jsons')

# Open the CSV file in read mode
file = open('example.csv', 'r')

# Create a reader object
csvReader = csv.reader(file)

# Print the type of reader object
print(type(csvReader))

# Convert reader object into a list
csvData = list(csvReader)

# Print all rows from the CSV file
print("CSV Data: ")
print(csvData)

# Move cursor back to beginning of file as the list method already used all the data from csv reader
file.seek(0)

# Loop through each row in the CSV file
print("\ndata after looping:")
for row in csvReader:

    # Print the complete row
    print('Row:', str(row))

    # Print individual columns
    print('First column:', str(row[0]))
    print('Second column:', str(row[1]))

# Close the file
file.close()