import openpyxl, os 
from openpyxl.styles import Font

os.chdir('.\\12. Spreadsheets')

wb = openpyxl.Workbook()
sheet = wb.active

italic24Font = Font(size=24, italic=True)

# We can you this much of styling here
# Font(
#     size=24,
#     italic=True,
#     bold=True,
#     color='FF0000'
# )

# styleObj = Style(font=italic24Font)                           # this font styling is depreciated form teh book
# sheet['A'].style/styleObj

sheet['A1'] = 'Hello World!'
sheet['A1'].font = italic24Font


# Adjusting Rows and Columns
sheet.row_dimensions[1].height = 70
sheet.column_dimensions['B'].width = 90


# Merging Cells
sheet['C3'] = 'Merged cell of 12'
sheet.merge_cells('C3:G5')
# use unmerge_cells to unmerge the columns
# sheet.unmerge_cells('C3:G5')


# Freeze Panes
sheet['A1'] = "First Column"
sheet['B1'] = "Second Column"
sheet['C1'] = "Third Column"

sheet.freeze_panes = 'A2'

# freeze_panes setting        Rows and columns frozen
# 'A2'                        Row 1
# 'B1'                        Column A
# 'C1'                        Column A & B
# 'C2'                        Row 1 and Column A & B
# 'A1' or None                None


wb.save('styled.xlsx')
