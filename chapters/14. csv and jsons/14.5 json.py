# This file explains how to read JSON data using json.loads()
# and convert Python objects into JSON strings using json.dumps().

import json

# JSON data stored as a string
jsonData = '{"name": "Sandesh", "age": 21, "city": "Nagpur"}'

# Convert JSON string into Python dictionary
pythonData = json.loads(jsonData)

# Print Python data
print("Python Dictionary:")
print(pythonData)

# Access values from dictionary
print("\nName:", pythonData['name'])
print("Age:", pythonData['age'])

# Python dictionary
studentData = {
    'name': 'Rahul',
    'age': 22,
    'city': 'Pune'
}

# Convert Python dictionary into JSON string
jsonString = json.dumps(studentData)

# Print JSON string
print("\nJSON String:")
print(jsonString)