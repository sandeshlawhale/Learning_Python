import openpyxl, os
from openpyxl.chart import BarChart, Reference, Series

os.chdir('.\\12. Spreadsheets')


wb = openpyxl.Workbook()
sheet= wb.active

for i in range(1,11):
    sheet['A'+str(i)] = i

# the below method is mentioned in the book is depriciated
# refObj = openpyxl.chart.Reference(sheet, (1,1), (10,1))
# seriesObj = openpyxl.charts.Series(refObj, title='first series')

# chartObj = openpyxl.charts.BarChart()
# chartObj.append(seriesObj)

# chartObj.drawing.top = 50
# chartObj.drawing.left = 100
# chartObj.drawing.width = 300
# chartObj.drawing.height = 200

# Create reference object
refObj = Reference(sheet,
                   min_col=1,
                   min_row=1,
                   max_col=1,
                   max_row=10)

# Create series
seriesObj = Series(refObj, title='First Series')

# Create chart
chartObj = BarChart()
chartObj.series.append(seriesObj)

# Chart size
chartObj.width = 15
chartObj.height = 10

sheet.add_chart(chartObj, "C5")
wb.save('sampleChart.xlsx')


