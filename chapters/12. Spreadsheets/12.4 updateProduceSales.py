# updateProduceSales.py - corrects costs in produce sales spreadsheet

# Garlic -> 3.07
# Celery -> 1.19
# Lemon -> 1.27

import openpyxl, os
os.chdir('.\\12. Spreadsheets')

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active

PRICE_UPDATES = {
    'Garlic': 3.07,
    'Celery': 1.19,
    'Lemon': 1.27
}

for i in range(2, sheet.max_row):
    produceName = sheet.cell(row=i, column=1).value

    if produceName in PRICE_UPDATES:
        sheet.cell(row=i, column=2).value = PRICE_UPDATES[produceName]

wb.save('updatedProduceSales.xlsx')