# readCensus.py - Tabulates population and number of census tracts for each county.

import openpyxl, os, pprint
os.chdir('.\\12. Spreadsheets')

print('Opening Workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')

sheet = wb['Population by Census Tract']

countyData = {}

print("Reading Data...")
for row in range(2, sheet.max_row + 1):
    state = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('writting data...')
print('all data = ', pprint.pformat(countyData))