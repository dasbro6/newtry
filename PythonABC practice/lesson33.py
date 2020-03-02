import openpyxl
from openpyxl.chart import(
Reference,
Series,
PieChart,
BarChart,
BubbleChart
)

workbook33 = openpyxl.Workbook()

sheetone = workbook33.active
sheetone.title = 'piechart'

dataone = [
    ['Pie', 'Sold'],
    ['Apple', 50],
    ['Cherry', 30],
    ['Pumpkin', 10],
    ['Chocolate', 40],
]

for row in dataone:
    sheetone.append(row)


c_pie=PieChart()
pie_labels = Reference(sheetone,min_col = 1,max_row = 2, min_row =5)
pie_data = Reference(sheetone,min_col = 2,max_row = 2, min_row =5)
c_pie.add_data(pie_data)
c_pie.set_categories(pie_labels)
sheetone.add_chart(c_pie,'A15')

workbook33.save('temp004.xlsx')
print('The program completed')

